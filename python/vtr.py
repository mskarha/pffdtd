import vtracer

inp = "/home/ta-user/pffdtd/python/output_frames_folder/frame_0090.png"
out = "out.svg"

vtracer.convert_image_to_svg_py(inp,
                                out,
                                colormode = 'binary',        # ["color"] or "binary"
                                hierarchical = 'stacked',   # ["stacked"] or "cutout"
                                mode = 'spline',            # ["spline"] "polygon", or "none"
                                filter_speckle = 4,         # default: 4
                                color_precision = 6,        # default: 6
                                layer_difference = 16,      # default: 16
                                corner_threshold = 60,      # default: 60
                                length_threshold = 4.0,     # in [3.5, 10] default: 4.0
                                max_iterations = 10,        # default: 10
                                splice_threshold = 45,      # default: 45
                                path_precision = 3          # default: 8
                                )
