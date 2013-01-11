"""

Filename: voxel_render.py
Author: Jason Cramer

The classes and functions responsible for rendering the voxel grid.

"""

from voxel_grid import *

class VoxelCamera(object):
    """
    The camera that renders the voxel grid.
    """

    def __init__(self):
        # Set position variables
        self._x = 0
        self._y = 0
        self._z = 0

        # Set rotation variables. For mathematical legitness,
        # rotation will be from 0 to 2pi degrees.
        self._rotx = 0
        self._roty = 0
        self._rotz = 0


        pass

    # Accessors, so we can set bounds on position and rotation

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_z(self), z):
        self._z = z

    def offset_x(self, dx):
        self._x += dx

    def offset_y(self, dy):
        self._y += dy

    def offset_z(self, dz):
        self._z += dz

    def set_rotx(self, rotx):
        self._rotx = rotx % (2*pi)

    def set_roty(self, roty):
        self._roty = roty % (2*pi)

    def set_rotz(self), rotz):
        self._rotz = rotz % (2*pi)

    def offset_x(self, dx):
        self._x = (self._rotx + dx) % (2*pi)

    def offset_y(self, dy):
        self._y = (self._roty + dy) % (2*pi)

    def offset_z(self, dz):
        self._z = (self._rotz + dz) % (2*pi)



    def draw_voxel(self, point, rgb):
        """
        Draw a single voxel.
        """

        # This will have to account for perspective and stuff, and only
        # draw things that are necessary. This is probably where all
        # the math comes in.

    def render(self, grid):
        """
        Return an OpenCV image with the rendered view.
        """
        # Based on camera coordinates
        
        # Create a new image to draw the rendered stuff on
        rendered = CreateImage((width, height), cv.IPL_DEPTH_8U, 3)

        # For now, just base on straight on angle
        # Since z is the most variable direction in terms of how
        # big it is, we'll make it the outer loop so we don't go
        # into a loop that potentially could only be depth 1
        for z in range(grid.length()):
            for y in range(grid.height()): 
                for x in range(grid.depth()):
                    # Get the RGB value
                    rgb = grid.get_rgb(x,y,z) 
                    
                    if not rgb:
                        # skip if no voxel
                        continue
                    # Draw the voxel    
                    draw_voxel((x,y,z),rgb,rendered) 
         return rendered
