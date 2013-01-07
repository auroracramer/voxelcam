"""

Filename: image.py
Author: Jason Cramer

The classes and functions that handle the image processing and computer vision operations of VoxelCam.

"""

import cv
from numpy import *

def pixelate_mat(img, blocksize=10):
    """
    Returns a matrix of the downsampled image. Averages pixels in blocks
    of a specified size to obtain the pixel values.
    """

    # Smooth image first to remove noise
    img_smooth = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 3)
    cv.Smooth(img, img_smooth, cv.CV_GAUSSIAN, 3, 3)

    # Convert the img to a numpy matrix
    mat = asarray(cv.GetMat(img_smooth))

    output = zeros((img_smooth.width/blocksize, img_smooth.height/blocksize, 3))

    # Loop through the blocks
    for x_pix in range(img.width/blocksize):
        for y_pix in range(img.height/blocksize):
            # Initialize/reset RGB sums
            red_sum = 0
            green_sum = 0
            blue_sum = 0

            # Loop through the block pixels
            for x in range(blocksize):
                for y in range(blocksize):
                    pixel = mat[y_pix*blocksize + y, x_pix*blocksize + x]
                    
                    # Add to the sum of RGB values in a block
                    red_sum += pixel[2]
                    green_sum += pixel[1]
                    blue_sum += pixel[0]

            # Average the RGB values for the block
            red = int(red_sum / (blocksize**2))
            green = int(green_sum / (blocksize**2))
            blue = int(blue_sum / (blocksize**2))

            # Store the value in the output matrix
            output[x_pix, y_pix] = array([red, green, blue])
 
    return output

def pixelate_img(img, blocksize=10):
    # Get pixelated matrix
    mat = pixelate_mat(img, blocksize)

    width = mat.shape[1]
    height = mat.shape[0]

    # Create an image to hold the pixelate image
    piximg = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 3)

    # Draw image onto our image object
    for x in range(width):
        for y in range(height):
            red = mat[x,y][0]
            green = mat[x,y][1]
            blue = mat[x,y][2]

            cv.Rectangle(piximg, (x*blocksize,y*blocksize), ((x+1) * blocksize, (y+1)*blocksize), cv.CV_RGB(red,green,blue), cv.CV_FILLED, 8, 0)

    return piximg
            

