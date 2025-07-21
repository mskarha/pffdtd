import cv2
import os
import requests
from pathlib import Path
from requests.auth import HTTPBasicAuth

# === CONFIGURATION ===
VIDEO_PATH = 'ghtestv4.mp4'  # Path to your MP4 file
OUTPUT_DIR = Path('svg_frames')  # Directory to save the SVGs
API_ID = 'vkzfkt6bg59ydvf'  # Replace with your actual API Id
API_SECRET = 'sf8jm733d83o649u29n5v1dhnn3udj8k7106jmvknfssm4bjh1pe'  # Replace with your actual API Secret
VECTORIZE_ENDPOINT = 'https://vectorizer.ai/api/v1/vectorize'

# === PREPARE OUTPUT DIRECTORY ===
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# === OPEN VIDEO FILE ===
video_capture = cv2.VideoCapture(VIDEO_PATH)

if not video_capture.isOpened():
    raise IOError(f"Cannot open video file: {VIDEO_PATH}")

frame_index = 0

while True:
    success, frame = video_capture.read()
    if not success:
        break  # No more frames

    # Save the current frame as a temporary PNG
    temp_image_path = OUTPUT_DIR / f'frame_{frame_index:05d}.png'
    cv2.imwrite(str(temp_image_path), frame)

    # Prepare the image file for upload
    with open(temp_image_path, 'rb') as image_file:
        files = {'image': image_file}
        auth = HTTPBasicAuth(API_ID, API_SECRET)

        data = {'mode': 'test'}  # Add this line

        response = requests.post(
            VECTORIZE_ENDPOINT,
            files=files,
            data=data,
            auth=auth
        )


        if response.status_code == 200:
            # Save returned SVG
            svg_filename = OUTPUT_DIR / f'frame_{frame_index:05d}.svg'
            with open(svg_filename, 'wb') as svg_file:
                svg_file.write(response.content)
            print(f"[✓] Vectorized frame {frame_index} → {svg_filename.name}")
        else:
            print(f"[!] Failed to vectorize frame {frame_index}: {response.status_code} {response.text}")

    # Optionally delete the temporary PNG
    os.remove(temp_image_path)
    frame_index += 1

# === CLEANUP ===
video_capture.release()
print("✅ All frames processed.")
