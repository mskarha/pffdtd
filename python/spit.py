import h5py
import json
import itertools

# Open the HDF5 file and retrieve the datasets
with h5py.File('../data/sim_data/aspen/gpu/vox_out.h5', 'r') as file:
    xv = file['/xv'][:]
    yv = file['/yv'][:]
    zv = file['/zv'][:]
    
    print("xv size:", xv.size) 
    print("yv size:", yv.size) 
    print("zv size:", zv.size) 
    print("Total points:", xv.size * yv.size * zv.size)

# Create the JSON structure
receivers = []

# Generate all (x, y, z) combinations and populate the JSON structure every 2161st coordinate
for i, (x, y, z) in enumerate(itertools.product(xv, yv, zv)):
    if i % 2161 == 0:  # Only append every 2161st coordinate
        receivers.append({
            "xyz": [float(x), float(y), float(z)],  # Ensure values are floats for JSON compatibility
            "name": ""
        })

# Write the data to a JSON file
output_data = {"receivers": receivers}

with open('voxel_grid.json', 'w') as jsonfile:
    json.dump(output_data, jsonfile, indent=4)

print("Voxel grid saved to voxel_grid.json")


