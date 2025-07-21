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
# Description: this shows a simple setup with FCC scheme, for visualization purposes
#
##############################################################################
from sim_setup import sim_setup

sim_setup(
    model_json_file='../ghtest/model_export.json',
    mat_folder='../data/materials',
    source_num=1,
    insig_type='hann10',
    diff_source=False,
    mat_files_dict={
                    }, #see build_mats.py to set these material impedances from absorption data
    duration=0.3,
    Tc=20,
    rh=50,
    fcc_flag=True,
    PPW=5.6, #for 2% phase velocity error at fmax
    fmax=5000.0,
    save_folder='../data/sim_data/ghtest/viz',
    compress=0,
    draw_vox=True,
    draw_backend='polyscope', #will draw 'voxelization' with polyscope (in which small white spheres denote rigid boundary nodes)
)

#then run with python and 3D visualization:
#   python3 -m fdtd.sim_fdtd --data_dir='../data/sim_data/ghtest/viz' --plot --draw_backend='mayavi' --json_model='../ghtest/model_export.json'
