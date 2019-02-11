import os
import cv2
import numpy as np

direc='source' #file location
count=1 # sequence number
for img in os.listdir(direc): # read file one by one
    f1=cv2.imread('source/'+img) # read images
    #file='test'+'/'+img
    cv2.imwrite("target/"+"%d.jpg" % count, f1) # write images to folder target
    count=count+1 # increment
