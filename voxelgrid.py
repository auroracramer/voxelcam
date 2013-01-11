"""

Filename: voxelgrid.py
Author: Jason Cramer

The main data structure for the voxel grid.

"""

from cv import *

class VoxelGrid(object):
    def __init__(length, height, depth):
        """
        Initializes a VoxelGrid container object with the dimensions
        of the 3D grid.

        length = x
        height = y
        depth  = z
        """

        # OpenCV Mat object, starts out with nonsense values
        self._grid = CreateMatND((length, height, depth), CV_32FC3)
        # is this really necessary? since we're replacing it when we
        # generate the grid.

    def size(self):
        """
        Return a tuple of the dimensions of this grid
        """

        return GetDims(self._grid)
        
    def matrix(self):
        """
        Return the Matrix object contained by this VoxelGrid object.
        """
        return self._grid
        
    def length(self):
        """
        Return the length (x dimension) of the grid.
        """
        return self.size()[0]

    def height(self):
        """
        Return the height (y dimension) of the grid.
        """
        return self.size()[1]

    def depth(self):
        """
        Return the depth (z dimension) of the grid.
        """
        return self.size()[2]

    def generate(color_matrix, geometry=None):
        """
        Generate the voxel grid based on the geometry and color matrix.
        Returns nothing. NOTHING I SAY!
        """
        # Remember that image pixel coordinates start from the top left

        # If no geometry is passed in, just make a flat voxel grid
        if not geometry:
            _grid = CreateMatND(GetDims(mat) + (1,), mat.type)
            # Account for the different origin by flipping the matrix
            Flip(color_matrix, _grid)

    def get_rgb(self, x, y, z):
        """
        Return the RGB value at a specific point. If
        the RGB values are negative, return None, as
        negative RGB values represent an absence of
        a voxel.
        """
        # Get the RGB value, and put in proper RGB order
        vox = tuple(reversed(self._grid[x,y,z]))
        
        if vox[0] < 0 or vox[1] < 0 or vox[2] < 0:
            # Return None if negative RGB
            return None

        return vox 
