"""

Filename: voxelgrid.py
Author: Jason Cramer

The main data structure for the voxel grid.

"""

from numpy import *
from numpy.linalg import *

class VoxelGrid(object):
    def __init__(length, height, depth):
        self._grid = zeros((length, height, depth, 3)

    def size(self):
        return self._grid.shape
        
    def grid(self):
        return self._grid
        
    def get_rgb(self, x, y, z):
        return self._grid[x,y,z] 
