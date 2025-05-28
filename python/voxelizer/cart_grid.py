##############################################################################
# This file is a part of PFFDTD.
#
# PFFTD is released under the MIT License.
# For details see the LICENSE file.
#
# Copyright 2021 Brian Hamilton.
#
# File name: cart_grid.py
#
# Description: This is a class for a Cartesian grid with grid spacing 'h' and
# some bounds.  Saves minimal data in HDF5 file if needed outside.
# 
##############################################################################

import numpy as np
from numpy import array as npa
from pathlib import Path
import h5py

class CartGrid():
    def __init__(self,h=None,offset=None,bmin=None,bmax=None,fcc=False):
        assert h is not None
        assert offset is not None
        assert bmin is not None #bbox min
        assert bmax is not None #bbox max

        #ensure three-layer halo, for ABCs, etc.
        assert offset>2.0 #distance offset

        xyzmin0 = bmin - offset*h
        xyzmax0 = bmax + offset*h

        #64-bit ints signed (for simplicity and numpy indexing)
        Nx,Ny,Nz = np.int_(np.ceil((xyzmax0 - xyzmin0)/h))+1
        if fcc: #make all dims even (so we can rotate any and halve)
            Nx += (Nx%2)
            Ny += (Ny%2)
            Nz += (Nz%2)
            self.print(f'To use FCC subgrid')

        #grid vectors
        xv,yv,zv = np.ogrid[0.:Nx,0.:Ny,0.:Nz]

        xv = xv.ravel()*h + xyzmin0[0]
        yv = yv.ravel()*h + xyzmin0[1]
        zv = zv.ravel()*h + xyzmin0[2]

        xyzmin = np.array([xv[0],yv[0],zv[0]])
        xyzmax = np.array([xv[-1],yv[-1],zv[-1]])

        assert np.all(xyzmin==xyzmin0)
        assert np.all(xyzmax>=xyzmax0)

        self.print(f'{Nx=}, {Ny=}, {Nz=}, N_grid_pts={Nx*Ny*Nz:g}')
        if fcc:
            self.print(f'{Nx*Ny*Nz/(2**28):.3f}GB in two-grid fcc single')
            self.print(f'{Nx*Ny*Nz/(2**27):.3f}GB in two-grid fcc double')
        else:
            self.print(f'{Nx*Ny*Nz/(2**27):.3f}GB in two-grid cart single')
            self.print(f'{Nx*Ny*Nz/(2**26):.3f}GB in two-grid cart double')

        self.h = h
        self.offset = offset
        self.xv = xv
        self.yv = yv
        self.zv = zv
        self.Nx = Nx
        self.Ny = Ny
        self.Nz = Nz
        self.Nxyz = npa([Nx,Ny,Nz])
        self.Npts = np.prod(self.Nxyz)
        self.xyzmin = xyzmin
        self.xyzmax = xyzmax

    def print(self,fstring):
        print(f'--CART_GRID: {fstring}')

    #don't use this unless grid is small 
    def draw_gridpoints(self,backend='mayavi'):
        xv = self.xv  
        yv = self.yv  
        zv = self.zv  
        h = self.h  

        X,Y,Z = np.meshgrid(xv,yv,zv,indexing='ij')
        if backend=='mayavi':
            from mayavi import mlab
            mlab.points3d(X.flat[:],Y.flat[:],Z.flat[:],color=(0,0,0),mode='sphere',resolution=4,scale_factor=h/4)
            mlab.draw()
        else:
            raise #todo polyscope

    def print_stats(self):
        #from fdtd.sim_comms import get_linear_interp_weights  # Ensure the function is imported
        cg = self
        cg.fcc = 1
        self.print(f'{cg.h=}')
        self.print(f'{cg.Nxyz=}')
        self.print(f'{cg.Npts=}')
        self.print(f'{cg.xyzmin=}')
        self.print(f'{cg.xyzmax=}')
            # Import the function locally to avoid circular dependency
        try:
            from fdtd.sim_comms import SimComms
            from common.myfuncs import ind2sub3d
            Nx = self.Nx
            Ny = self.Ny
            Nz = self.Nz
            weights, pos = SimComms.get_linear_interp_weights(self, cg.xyzmin)
            self.print(f'get_linear_interp_weights(cg.xyzmin)_weights: {weights}')
            self.print(f'get_linear_interp_weights(cg.xyzmin)_pos: {pos}')
            pos_ix,pos_iy,pos_iz = ind2sub3d(pos,Nx,Ny,Nz)
            self.print(f'ind2sub3d(pos_min): {min(pos_ix),min(pos_iy),min(pos_iz)}')
            weights, pos = SimComms.get_linear_interp_weights(self, cg.xyzmax-.1)
            self.print(f'get_linear_interp_weights(cg.xyzmax)_weights: {weights}')
            self.print(f'get_linear_interp_weights(cg.xyzmax)_pos: {pos}')
            pos_ix,pos_iy,pos_iz = ind2sub3d(pos,Nx,Ny,Nz)
            self.print(f'ind2sub3d(pos_max): {max(pos_ix),max(pos_iy),max(pos_iz)}')
        except ImportError as e:
            self.print(f"Error importing get_linear_interp_weights: {e}")
            

    #save in HDF5 file
    def save(self,save_folder):
        xv = self.xv  
        yv = self.yv  
        zv = self.zv  
        h = self.h  

        save_folder = Path(save_folder)
        self.print(f'{save_folder=}')
        if not save_folder.exists():
            save_folder.mkdir(parents=True)
        else:
            assert save_folder.is_dir()

        kw = {'compression': "gzip", 'compression_opts': 9}
        h5f = h5py.File(save_folder / Path('cart_grid.h5'),'w')
        h5f.create_dataset('xv', data=xv, **kw)
        h5f.create_dataset('yv', data=yv, **kw)
        h5f.create_dataset('zv', data=zv, **kw)
        h5f.create_dataset('h', data=np.float64(h))
        h5f.close()
