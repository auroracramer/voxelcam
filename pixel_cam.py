"""

Filename: pixel_cam.py
Author: Jason Cramer

Pixelizes a webcam feed.

"""
from image import *

class PixelCam(object):
    def __init__(self):
        self.capture = cv.CreateCameraCapture(-1)

    def start(self):
        cv.NamedWindow("PixelCam", cv.CV_WINDOW_AUTOSIZE)
        cv.MoveWindow("PixelCam", 600, 200)
        while True:
            rawframe = cv.QueryFrame(self.capture)
            if not rawframe:
                break
            frame = cv.CreateImage((rawframe.width, rawframe.height), cv.IPL_DEPTH_8U, 3)
            cv.Resize(rawframe,frame)
            img = pixelate_img(frame)
            cv.ShowImage("PixelCam", img)
            c = cv.WaitKey(33)
            if c == 27:
                break
        cv.DestroyWindow("PixelCam")

