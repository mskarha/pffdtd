import cv2
import os
import argparse
import vtracer
import numpy as np

def extract_and_convert_frames_to_svg(video_path, output_folder):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    print(f"Total frames: {frame_count}, FPS: {fps}")

    frame_index = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Skip if frame is invalid or unreadable
        if frame is None or frame.shape[0] == 0 or frame.shape[1] == 0:
            print(f"⚠️ Skipping unreadable frame at index {frame_index}")
            frame_index += 1
            continue

        # Step 1: Convert BGR to BGRA
        frame_bgra = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        # Step 2: Create masks
        white_mask = cv2.inRange(frame, (200, 200, 200), (255, 255, 255))
        non_white_mask = cv2.inRange(frame, (0, 0, 0), (199, 199, 199))

        # Step 3: Apply masks to BGRA
        frame_bgra[:, :, 0:3][non_white_mask > 0] = [0, 0, 0]
        frame_bgra[:, :, 3] = np.where(white_mask == 255, 0, 255)

        # Step 4: Sanity check — if resulting frame is all transparent or all black
        if not frame_bgra[:, :, :3].any():
            print(f"⚠️ Skipping fully black frame at index {frame_index}")
            frame_index += 1
            continue

        # Save the PNG
        temp_png_file = os.path.join(output_folder, f"temp_frame_{frame_index:04d}.png")
        cv2.imwrite(temp_png_file, frame_bgra)

        # Convert to SVG
        output_svg_file = os.path.join(output_folder, f"frame_{frame_index:04d}.svg")
        try:
            vtracer.convert_image_to_svg_py(
                temp_png_file,
                output_svg_file,
                colormode='color',
                hierarchical='stacked',
                mode='polygon',
                filter_speckle=0
            )
            print(f"✅ Converted to SVG: {output_svg_file}")
        except Exception as e:
            print(f"❌ Error converting frame {frame_index}: {e}")

        # Cleanup
        if os.path.exists(temp_png_file):
            os.remove(temp_png_file)

        frame_index += 1


    video.release()
    print(f"SVG frames saved to {output_folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from an MP4 video, convert to SVG, and save.")
    parser.add_argument("video", help="Path to the input MP4 video file.")
    parser.add_argument("output_folder", help="Path to the folder where SVG files will be saved.")
    args = parser.parse_args()

    extract_and_convert_frames_to_svg(args.video, args.output_folder)

