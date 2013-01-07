"""

Filename: image.py
Author: Jason Cramer

The classes and functions that handle the image processing and computer vision operations of VoxelCam.

"""

import cv
from numpy import *

def pixelate_mat(img, blocksize=10, smoothing=False):
    """
    Returns a matrix of the downsampled image. Averages pixels in blocks
    of a specified size to obtain the pixel values.
    """

    if smoothing:
        # Smooth image first to remove noise
        img = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 3)
        cv.Smooth(img, img_smooth, cv.CV_GAUSSIAN, 3, 3)

    # Get the matrix
    mat = cv.GetMat(img)

    output = zeros((img.height/blocksize, img.width/blocksize, 3))

    # Loop through the blocks
    for x_pix in range(img.width/blocksize):
        for y_pix in range(img.height/blocksize):
            xstart = x_pix * blocksize
            ystart = y_pix * blocksize

            # Average the RGB values for the block
            average = cv.Avg(mat[ystart:ystart+blocksize, xstart:xstart+blocksize])

            red = average[2]
            green = average[1]
            blue = average[0]

            # Store the value in the output matrix
            output[y_pix, x_pix] = array([red, green, blue])
 
    return output


def pixelate_img(img, blocksize=10, smoothing=False):
    """
    Returns the downsampled image. Averages pixels in blocks
    of a specified size to obtain the pixel values.
    """

    if smoothing:
        # Smooth image first to remove noise
        img = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 3)
        cv.Smooth(img, img_smooth, cv.CV_GAUSSIAN, 3, 3)

    # Get the matrix
    mat = cv.GetMat(img)

    width = img.width/blocksize * blocksize
    height = img.height/blocksize * blocksize

    # Create an image to hold the pixelate image
    piximg = cv.CreateImage((width, height), cv.IPL_DEPTH_8U, 3)

    # Loop through the blocks
    for x_pix in range(width/blocksize):
        for y_pix in range(height/blocksize):
            xstart = x_pix * blocksize
            ystart = y_pix * blocksize

            # Average the RGB values for the block
            average = cv.Avg(mat[ystart:ystart+blocksize, xstart:xstart+blocksize])

            red = average[2]
            green = average[1]
            blue = average[0]

            cv.Rectangle(piximg, (x_pix*blocksize,y_pix*blocksize), ((x_pix+1) * blocksize, (y_pix+1)*blocksize), cv.CV_RGB(red,green,blue), cv.CV_FILLED, 8, 0)
 
    return piximg
            

