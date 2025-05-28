##############################################################################
# This file is a part of PFFDTD.
#
# PFFTD is released under the MIT License.
# For details see the LICENSE file.
#
# Copyright 2021 Brian Hamilton.
#
# File name: test_script_aspenexg_fcc_viz.py
#
# Description: this shows a simple setup with FCC scheme, for visualization purposes
#
##############################################################################
from sim_setup import sim_setup

sim_setup(
    model_json_file='../aspenexgchoir/model_export.json',
    mat_folder='../data/materials',
    source_num=1,
    insig_type='dhann30',
    diff_source=False,
    mat_files_dict={
'Audience Reflectors': 'Audience Reflectors.h5',
'Bells': 'Bells.h5',
'BOH Closure': 'BOH Closure.h5',
'Choir Loft Carpeted Floor': 'Choir Loft Carpeted Floor.h5',
'Choir Loft Facing': 'Choir Loft Facing.h5',
'Choir Loft Stairs': 'Choir Loft Stairs.h5',
'Concrete Floor': 'Concrete Floor.h5',
'Concrete Stairs': 'Concrete Stairs.h5',
'Concrete Stepped Floor': 'Concrete Stepped Floor.h5',
'Louver Walls': 'Louver Walls.h5',
'Offstage': 'Offstage.h5',
'Offstage Ceiling': 'Offstage Ceiling.h5',
'Overstage Reflectors': 'Audience Reflectors.h5',
'SEATING - PAD': 'SEATING - PAD.h5',
'SEATING - PAD REMOVE': 'SEATING - PAD REMOVE.h5',
'SEATING - REAR': 'SEATING - REAR.h5',
'SEATING - REAR REMOVE': 'SEATING - REAR REMOVE.h5',
'Soundboth Walls': 'Soundboth Walls.h5',
'Stage': 'Stage.h5',
'Stage Stairs': 'Stage Stairs.h5',
'Stagehouse Roof': 'Stagehouse Roof.h5',
'Structure': 'Structure.h5',
'Tent': 'Tent.h5',
'Tent - Out of Bounds': 'Tent - Out of Bounds.h5',
'Upstage Walls - Back and Top': 'Upstage Walls - Back and Top.h5',
'Upstage Walls - Lower': 'Upstage Walls - Lower.h5',
'Upstage Walls - Upper': 'Upstage Walls - Upper.h5',
'Wood Ceiling': 'Wood Ceiling.h5',
                    }, #see build_mats.py to set these material impedances from absorption data
    duration=0.65,
    Tc=20,
    rh=50,
    fcc_flag=True,
    PPW=5.6, #for 2% phase velocity error at fmax
    fmax=1000.0,
    save_folder='../data/sim_data/aspenexgchoir/viz',
    compress=0,
    draw_vox=True,
    draw_backend='polyscope', #will draw 'voxelization' with polyscope (in which small white spheres denote rigid boundary nodes)
)

#then run with python and 3D visualization:
#   python3 -m fdtd.sim_fdtd --data_dir='../data/sim_data/aspenexgchoir/viz' --plot --draw_backend='mayavi' --json_model='../aspenexg/model_export.json'
