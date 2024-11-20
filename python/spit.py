import h5py
import json
import itertools
import time

# Open the HDF5 file and retrieve the datasets
with h5py.File('../data/sim_data/aspen/gpu/vox_out.h5', 'r') as file:
    xv = file['/xv'][:]
    yv = file['/yv'][:]
    zv = file['/zv'][:]
    
    print("xv size:", xv.size) 
    print("yv size:", yv.size) 
    print("zv size:", zv.size) 
    print("Total points:", xv.size * yv.size * zv.size)

# Track time to print progress every 10 seconds
start_time = time.time()

# Open JSON file for writing and start writing the array structure
with open('voxel_grid.json', 'w') as jsonfile:
    jsonfile.write('{"receivers": [\n')

    first_entry = True
    for i, (x, y, z) in enumerate(itertools.product(xv, yv, zv)):
        # Only process every 2161st coordinate
        if i % 2161 == 0:
            if not first_entry:
                jsonfile.write(",\n")  # Separate entries with a comma
            jsonfile.write(json.dumps({
                "xyz": [float(x), float(y), float(z)],
                "name": ""
            }))
            first_entry = False
        
        # Print progress every 10 seconds
        if time.time() - start_time >= 10:
            print(f"Progress: i = {i}")
            start_time = time.time()  # Reset the timer

    # Close JSON array structure
    jsonfile.write('\n]}')

print("Voxel grid saved to voxel_grid.json")

