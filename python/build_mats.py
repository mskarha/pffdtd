##############################################################################
# This file is a part of PFFDTD.
#
# PFFTD is released under the MIT License.
# For details see the LICENSE file.
#
# Copyright 2021 Brian Hamilton.
#
# File name: build_mats.py
#
# Description: Examples of setting/saving material impedances data
#
##############################################################################

import numpy as np
from pathlib import Path
from numpy import array as npa
from materials.adm_funcs import *

plot=False #set to True to see fits, but have to close plots to proceed to next material
write_folder = Path('../data/materials')
#some examples to save admittance/impedance data 
#these are Sabine coefficients, 16Hz to 16kHz centre frequencies
mv_chairs       = npa([0.22  , 0.22  , 0.22 , 0.22 , 0.26 , 0.3  , 0.33 , 0.34 , 0.34 , 0.34 , 0.34])
mv_floor        = npa([0.14  , 0.14  , 0.14 , 0.14 , 0.1  , 0.06 , 0.08 , 0.1  , 0.1  , 0.1  , 0.1])
mv_plasterboard = npa([ 0.15 ,  0.15 , 0.15 , 0.15 , 0.1  , 0.06 , 0.04 , 0.04 , 0.05 , 0.05 , 0.05])
mv_window       = npa([0.35  , 0.35  , 0.35 , 0.35 , 0.25 , 0.18 , 0.12 , 0.07 , 0.04 , 0.04 , 0.04])
mv_wood         = npa([0.25  , 0.25  , 0.25 , 0.25 , 0.15 , 0.1  , 0.09 , 0.08 , 0.07 , 0.07 , 0.07])
fit_to_Sabs_oct_11(mv_chairs       , filename=Path(write_folder / 'mv_chairs.h5')       , plot=plot)
fit_to_Sabs_oct_11(mv_floor        , filename=Path(write_folder / 'mv_floor.h5')        , plot=plot)
fit_to_Sabs_oct_11(mv_plasterboard , filename=Path(write_folder / 'mv_plasterboard.h5') , plot=plot)
fit_to_Sabs_oct_11(mv_window       , filename=Path(write_folder / 'mv_window.h5')       , plot=plot)
fit_to_Sabs_oct_11(mv_wood         , filename=Path(write_folder / 'mv_wood.h5')         , plot=plot)

#these are Sabine coefficients, 16Hz to 16kHz centre frequencies
ctk_acoustic_panel  = npa([0.2  ,  0.2   , 0.42  , 0.89  , 1     , 1     , 1     , 1     , 1     , 1     , 1])
ctk_altar           = npa([0.25 ,  0.25  , 0.25  , 0.25  , 0.15  , 0.1   , 0.09  , 0.08  , 0.07  , 0.07  , 0.07])
ctk_audience        = npa([0.1  ,  0.1   , 0.1   , 0.1   , 0.07  , 0.08  , 0.1   , 0.1   , 0.11  , 0.11  , 0.11])
ctk_carpet          = npa([0.08 ,  0.08  , 0.08  , 0.08  , 0.24  , 0.57  , 0.69  , 0.71  , 0.73  , 0.73  , 0.73])
ctk_ceiling         = npa([0.19 ,  0.19  , 0.19  , 0.19  , 0.06  , 0.05  , 0.08  , 0.07  , 0.05  , 0.05  , 0.05])
ctk_chair           = npa([0.44 ,  0.44  , 0.44  , 0.44  , 0.56  , 0.67  , 0.74  , 0.83  , 0.87  , 0.87  , 0.87])
ctk_tile            = npa([0.015,  0.015 , 0.015 , 0.015 , 0.015 , 0.005 , 0.005 , 0.005 , 0.005 , 0.005 , 0.005])
ctk_walls           = npa([0.19 ,  0.19  , 0.19  , 0.19  , 0.06  , 0.05  , 0.08  , 0.07  , 0.05  , 0.05  , 0.05])
ctk_window          = npa([0.35 ,  0.35  , 0.35  , 0.35  , 0.25  , 0.18  , 0.12  , 0.07  , 0.04  , 0.04  , 0.04])

fit_to_Sabs_oct_11(ctk_acoustic_panel , filename=Path(write_folder / 'ctk_acoustic_panel.h5') , plot=plot)
fit_to_Sabs_oct_11(ctk_altar          , filename=Path(write_folder / 'ctk_altar.h5')          , plot=plot)
fit_to_Sabs_oct_11(ctk_audience       , filename=Path(write_folder / 'ctk_audience.h5')       , plot=plot)
fit_to_Sabs_oct_11(ctk_carpet         , filename=Path(write_folder / 'ctk_carpet.h5')         , plot=plot)
fit_to_Sabs_oct_11(ctk_ceiling        , filename=Path(write_folder / 'ctk_ceiling.h5')        , plot=plot)
fit_to_Sabs_oct_11(ctk_chair          , filename=Path(write_folder / 'ctk_chair.h5')          , plot=plot)
fit_to_Sabs_oct_11(ctk_tile           , filename=Path(write_folder / 'ctk_tile.h5')           , plot=plot)
fit_to_Sabs_oct_11(ctk_walls          , filename=Path(write_folder / 'ctk_walls.h5')          , plot=plot)
fit_to_Sabs_oct_11(ctk_window         , filename=Path(write_folder / 'ctk_window.h5')         , plot=plot)

Audience_Reflectors = npa([0.34, 0.23, 0.35, 0.12, 0.02, 0.02, 0.03, 0.03, 0.01, 0.01, 0.01])
fit_to_Sabs_oct_11(Audience_Reflectors, filename=Path(write_folder / 'Audience Reflectors.h5'), plot=plot)

Audience_Shades = npa([0.13, 0.18, 0.11, 0.30, 0.64, 0.83, 0.99, 0.99, 0.99, 0.99, 0.99])
fit_to_Sabs_oct_11(Audience_Shades, filename=Path(write_folder / 'Audience Shades.h5'), plot=plot)

Bells = npa([0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.05, 0.05, 0.06])
fit_to_Sabs_oct_11(Bells, filename=Path(write_folder / 'Bells.h5'), plot=plot)

BOH_Closure = npa([0.34, 0.23, 0.35, 0.12, 0.02, 0.02, 0.03, 0.03, 0.01, 0.01, 0.01])
fit_to_Sabs_oct_11(BOH_Closure, filename=Path(write_folder / 'BOH Closure.h5'), plot=plot)

Choir_Loft_Carpeted_Floor = npa([0.01, 0.01, 0.02, 0.02, 0.03, 0.06, 0.10, 0.26, 0.47, 0.47, 0.99])
fit_to_Sabs_oct_11(Choir_Loft_Carpeted_Floor, filename=Path(write_folder / 'Choir Loft Carpeted Floor.h5'), plot=plot)

Choir_Loft_Facing = npa([0.19, 0.17, 0.15, 0.15, 0.11, 0.10, 0.07, 0.06, 0.07, 0.07, 0.05])
fit_to_Sabs_oct_11(Choir_Loft_Facing, filename=Path(write_folder / 'Choir Loft Facing.h5'), plot=plot)

Choir_Loft_Stairs = npa([0.01, 0.01, 0.02, 0.02, 0.03, 0.06, 0.10, 0.26, 0.47, 0.47, 0.99])
fit_to_Sabs_oct_11(Choir_Loft_Stairs, filename=Path(write_folder / 'Choir Loft Stairs.h5'), plot=plot)

Concrete_Floor = npa([0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.05, 0.05, 0.06])
fit_to_Sabs_oct_11(Concrete_Floor, filename=Path(write_folder / 'Concrete Floor.h5'), plot=plot)

Concrete_Stairs = npa([0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.05, 0.05, 0.06])
fit_to_Sabs_oct_11(Concrete_Stairs, filename=Path(write_folder / 'Concrete Stairs.h5'), plot=plot)

Concrete_Stepped_Floor = npa([0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.05, 0.05, 0.06])
fit_to_Sabs_oct_11(Concrete_Stepped_Floor, filename=Path(write_folder / 'Concrete Stepped Floor.h5'), plot=plot)

Louver_Walls = npa([0.10, 0.13, 0.15, 0.15, 0.25, 0.40, 0.55, 0.60, 0.60, 0.60, 0.99])
fit_to_Sabs_oct_11(Louver_Walls, filename=Path(write_folder / 'Louver Walls.h5'), plot=plot)

Offstage = npa([0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60])
fit_to_Sabs_oct_11(Offstage, filename=Path(write_folder / 'Offstage.h5'), plot=plot)

Offstage_Ceiling = npa([0.25, 0.19, 0.14, 0.14, 0.10, 0.06, 0.04, 0.04, 0.03, 0.03, 0.02])
fit_to_Sabs_oct_11(Offstage_Ceiling, filename=Path(write_folder / 'Offstage Ceiling.h5'), plot=plot)

SEATING___PAD = npa([0.33, 0.35, 0.35, 0.35, 0.45, 0.57, 0.61, 0.59, 0.55, 0.55, 0.69])
fit_to_Sabs_oct_11(SEATING___PAD, filename=Path(write_folder / 'SEATING - PAD.h5'), plot=plot)

SEATING___PAD_REMOVE = npa([0.33, 0.35, 0.35, 0.35, 0.45, 0.57, 0.61, 0.59, 0.55, 0.55, 0.69])
fit_to_Sabs_oct_11(SEATING___PAD_REMOVE, filename=Path(write_folder / 'SEATING - PAD REMOVE.h5'), plot=plot)

SEATING___REAR = npa([0.33, 0.35, 0.35, 0.35, 0.45, 0.57, 0.61, 0.59, 0.55, 0.55, 0.69])
fit_to_Sabs_oct_11(SEATING___REAR, filename=Path(write_folder / 'SEATING - REAR.h5'), plot=plot)

SEATING___REAR_REMOVE = npa([0.33, 0.35, 0.35, 0.35, 0.45, 0.57, 0.61, 0.59, 0.55, 0.55, 0.69])
fit_to_Sabs_oct_11(SEATING___REAR_REMOVE, filename=Path(write_folder / 'SEATING - REAR REMOVE.h5'), plot=plot)

Soundboth_Walls = npa([0.31, 0.25, 0.19, 0.19, 0.14, 0.09, 0.06, 0.06, 0.05, 0.05, 0.03])
fit_to_Sabs_oct_11(Soundboth_Walls, filename=Path(write_folder / 'Soundboth Walls.h5'), plot=plot)

Stage = npa([0.19, 0.17, 0.15, 0.15, 0.11, 0.10, 0.07, 0.06, 0.07, 0.07, 0.05])
fit_to_Sabs_oct_11(Stage, filename=Path(write_folder / 'Stage.h5'), plot=plot)

Stage_Stairs = npa([0.19, 0.17, 0.15, 0.15, 0.11, 0.10, 0.07, 0.06, 0.07, 0.07, 0.05])
fit_to_Sabs_oct_11(Stage_Stairs, filename=Path(write_folder / 'Stage Stairs.h5'), plot=plot)

Stagehouse_Roof = npa([0.10, 0.10, 0.10, 0.10, 0.07, 0.05, 0.06, 0.06, 0.06, 0.06, 0.05])
fit_to_Sabs_oct_11(Stagehouse_Roof, filename=Path(write_folder / 'Stagehouse Roof.h5'), plot=plot)

Structure = npa([0.15, 0.12, 0.05, 0.05, 0.10, 0.10, 0.10, 0.07, 0.02, 0.01, 0.02])
fit_to_Sabs_oct_11(Structure, filename=Path(write_folder / 'Structure.h5'), plot=plot)

Tent = npa([0.34, 0.23, 0.35, 0.12, 0.02, 0.02, 0.03, 0.03, 0.01, 0.01, 0.01])
fit_to_Sabs_oct_11(Tent, filename=Path(write_folder / 'Tent.h5'), plot=plot)

Tent___Out_of_Bounds = npa([0.34, 0.23, 0.35, 0.12, 0.02, 0.02, 0.03, 0.03, 0.01, 0.01, 0.01])
fit_to_Sabs_oct_11(Tent___Out_of_Bounds, filename=Path(write_folder / 'Tent - Out of Bounds.h5'), plot=plot)

Upstage_Walls___Back_and_Top = npa([0.25, 0.19, 0.14, 0.14, 0.10, 0.06, 0.04, 0.04, 0.03, 0.03, 0.02])
fit_to_Sabs_oct_11(Upstage_Walls___Back_and_Top, filename=Path(write_folder / 'Upstage Walls - Back and Top.h5'), plot=plot)

Upstage_Walls___Lower = npa([0.10, 0.10, 0.10, 0.10, 0.07, 0.05, 0.06, 0.06, 0.06, 0.06, 0.05])
fit_to_Sabs_oct_11(Upstage_Walls___Lower, filename=Path(write_folder / 'Upstage Walls - Lower.h5'), plot=plot)

Upstage_Walls___Upper = npa([0.10, 0.10, 0.10, 0.10, 0.07, 0.05, 0.06, 0.06, 0.06, 0.06, 0.05])
fit_to_Sabs_oct_11(Upstage_Walls___Upper, filename=Path(write_folder / 'Upstage Walls - Upper.h5'), plot=plot)

Wood_Ceiling = npa([0.10, 0.10, 0.10, 0.10, 0.07, 0.05, 0.06, 0.06, 0.06, 0.06, 0.05])
fit_to_Sabs_oct_11(Wood_Ceiling, filename=Path(write_folder / 'Wood Ceiling.h5'), plot=plot)


#freq-independent impedance from reflection coefficients
write_freq_ind_mat_from_Yn(convert_R_to_Yn(0.90),filename=Path(write_folder / 'R90_mat.h5'))
write_freq_ind_mat_from_Yn(convert_R_to_Yn(0.5),filename=Path(write_folder / 'R50.h5'))

#freq-independent impedance from Sabine abs coefficient
write_freq_ind_mat_from_Yn(convert_Sabs_to_Yn(0.5),filename=Path(write_folder / 'a50.h5'))

#input DEF values directly
write_freq_dep_mat(npa([[0,1.0,0],[2,3,4]]),filename=Path(write_folder / 'ex_mat.h5'))

#to read and plot a material file
#plot_DEF_admittance(np.logspace(np.log10(10),np.log10(20e3),4000),read_mat_DEF(write_folder/'chairs.h5'))
