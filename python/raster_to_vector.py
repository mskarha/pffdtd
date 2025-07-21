import cv2
import numpy as np
import svgwrite
from sklearn.cluster import KMeans

def raster_to_vector(input_image, output_svg, n_colors=5, threshold=128):
    # Load the image
    image = cv2.imread(input_image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize for faster processing (optional)
    original_size = image.shape[:2]
    resized_size = (256, int(256 * original_size[1] / original_size[0]))
    image = cv2.resize(image, resized_size)

    # Apply K-means clustering for color reduction
    reshaped_image = image.reshape((-1, 3))
    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(reshaped_image)
    clustered_image = kmeans.cluster_centers_[kmeans.labels_].reshape(image.shape).astype(np.uint8)

    # Convert to grayscale and apply thresholding
    grayscale = cv2.cvtColor(clustered_image, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(grayscale, threshold, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Create SVG file
    dwg = svgwrite.Drawing(output_svg, profile="tiny", size=(resized_size[1], resized_size[0]))
    for contour in contours:
        path_data = "M " + " L ".join(f"{p[0][0]},{p[0][1]}" for p in contour)
        dwg.add(dwg.path(d=path_data, fill="none", stroke="black", stroke_width=1))
    dwg.save()

    print(f"SVG saved to {output_svg}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert raster images to vector SVGs.")
    parser.add_argument("input_image", help="Path to the input PNG image.")
    parser.add_argument("output_svg", help="Path to save the output SVG file.")
    parser.add_argument("--n_colors", type=int, default=5, help="Number of colors for clustering (default: 5).")
    parser.add_argument("--threshold", type=int, default=128, help="Threshold for binarization (default: 128).")
    args = parser.parse_args()

    raster_to_vector(args.input_image, args.output_svg, args.n_colors, args.threshold)

