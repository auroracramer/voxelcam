#! /opt/local/bin/python27

from image import *

cv.NamedWindow("hello", cv.CV_WINDOW_AUTOSIZE)
cv.MoveWindow("hello", 600, 300)
img = cv.LoadImage("lena.jpeg")
piximg = pixelate_img(img)
cv.ShowImage("hello", piximg)
cv.WaitKey(10000)
cv.DestroyWindow("hello")

