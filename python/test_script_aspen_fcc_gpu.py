##############################################################################
# This file is a part of PFFDTD.
#
# PFFTD is released under the MIT License.
# For details see the LICENSE file.
#
# Copyright 2021 Brian Hamilton.
#
# File name: test_script_MV_fcc_viz.py
#
# Description: this shows a simple setup with FCC scheme, for a larger single-precision GPU run (<12GB VRAM)
#
##############################################################################
from sim_setup import sim_setup

sim_setup(
    model_json_file='../aspen/model_export.json',
    draw_backend='mayavi',
    mat_folder='../data/materials',
    source_num=1,
    insig_type='impulse',
    diff_source=True,
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
    duration=0.2,
    Tc=20,
    rh=50,
    fcc_flag=True,
    PPW=10.0, #for 1% phase velocity error at fmax
    fmax=1500.0,
    save_folder='../data/sim_data/aspen/gpu',
    save_folder_gpu='../data/sim_data/aspen/gpu',
    compress=3, #apply level-3 GZIP compression to larger h5 files
)

#then from '../data/sim_data/aspen/gpu' folder, run (relative path for default folder structure):
#   ../../../../c_cuda/fdtd_main_gpu_single.x

#then post-process with something like:
#   python -m fdtd.process_outputs --data_dir='../data/sim_data/aspen/gpu/' --fcut_lowpass 2500.0 --N_order_lowpass=8 --symmetric --fcut_lowcut 10.0 --N_order_lowcut=4 --air_abs_filter='stokes' --save_wav --plot
