import argparse
import PIL.ImageOps
from PIL import Image
import numpy as np
import potrace

# Function to convert Bezier curves into SVG path commands
def bezier_to_svg_path(start, control1, control2, end):
    return f"C {control1[0]},{control1[1]} {control2[0]},{control2[1]} {end[0]},{end[1]}"

def img_to_svg(input_path, output_path, threshold=50):
    # Load image
    image = Image.open(input_path).convert("L")  # Convert to grayscale
    
    # Invert colors
    image = PIL.ImageOps.invert(image)

    # Convert to binary array (black and white)
    bitmap_array = np.array(image) > threshold

    # Create potrace bitmap and trace paths
    bitmap = potrace.Bitmap(bitmap_array)
    path = bitmap.trace(turdsize=0, turnpolicy=potrace.TURNPOLICY_BLACK, alphamax=0.5, opticurve=1)

    # Prepare SVG elements
    svg_paths = []
    for curve in path:
        path_data = []
        start_point = curve.start_point
        path_data.append(f"M {start_point[0]} {start_point[1]}")  # Move to start point

        for segment in curve:
            if segment.is_corner:
                # Line to corner
                path_data.append(f"L {segment.c[0]} {segment.c[1]}")
            else:
                # Bezier curve
                path_data.append(bezier_to_svg_path(
                    start=path_data[-1][-2:],
                    control1=segment.c1,
                    control2=segment.c2,
                    end=segment.end_point
                ))
        
        path_data.append("Z")  # Close the path
        svg_paths.append(" ".join(path_data))

    # Write SVG file
    svg_header = f"<svg xmlns='http://www.w3.org/2000/svg' width='{bitmap_array.shape[1]}' height='{bitmap_array.shape[0]}' viewBox='0 0 {bitmap_array.shape[1]} {bitmap_array.shape[0]}'>"
    svg_footer = "</svg>"
    svg_content = "\n".join(f"<path d='{path}' fill='none' stroke='black' />" for path in svg_paths)

    with open(output_path, "w") as f:
        f.write(f"{svg_header}\n{svg_content}\n{svg_footer}")

    print(f"SVG saved to {output_path}")

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Vectorize a PNG image into SVG using pypotrace.")
    parser.add_argument("input", help="Path to the input PNG image.")
    parser.add_argument("output", help="Path to save the output SVG file.")
    parser.add_argument("--threshold", type=int, default=50, help="Threshold for binarization (default: 50).")
    args = parser.parse_args()

    # Run the vectorization
    img_to_svg(args.input, args.output, args.threshold)
