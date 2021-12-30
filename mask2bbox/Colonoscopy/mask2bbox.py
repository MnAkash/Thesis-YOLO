# -*- coding: utf-8 -*-
"""
This program will create bounding box for ground truth segmented mask.
Finally will create annotated txt file supported by YOLO


Created on Sun Oct  3 01:28:47 2021
@author: akash
"""

import glob
import numpy as np
from skimage import io
import cv2


def mask2bbox(main_image, mask_image, show_bbox=True, show_contour=False):
    box = []#define a bounding box list to store all
    
    # Load the main image
    image = cv2.imread(main_image)
    
    im_height, im_width, _ = image.shape
    
    # Load the mask image
    #since mask image is pure 2D B&W image, skimage is used to load it
    im = io.imread(mask_image)
    imarray = np.array(im)
    
    #detect contours
    contours, hierarchy = cv2.findContours(imarray,
      cv2.RETR_TREE,
      cv2.CHAIN_APPROX_SIMPLE)
    
    
    if show_contour:
        # Draw the contours on the original image and display the result
        # Input color code is in BGR (blue, green, red) format
        # -1 means to draw all contours
        with_contours = cv2.drawContours(image, contours, -1,(255,0,255),3)
    
    # x > starting x coordinate of the bounding box
    # y > starting y coordinate of the bounding box
    # w > width of the bounding box
    # h > height of the bounding box
     
    # Draw bounding boxs around all contours
    for c in contours:      
      # Make sure contour area is large enough
      if (cv2.contourArea(c)) > 10:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image,(x,y), (x+w,y+h), (0,0,255), 2)
        
        #===============normalize values for YOLO algorithm
        box.append([x/im_width ,y/im_height, w/im_width, h/im_height])
    
    if show_bbox:cv2.imshow('All contours with bounding box', image)
    return box

def xywh2yoloBox(x,y,w,h):
    # x > starting x coordinate of the bounding box
    # y > starting y coordinate of the bounding box
    # w > width of the bounding box
    # h > height of the bounding box
    
    #Yolo bounding box format
    #x_center, y_center, width, height
    
    x_center = x+(w/2)
    y_center = y+(h/2)
    width = w
    height = h
    
    return x_center, y_center, width, height


images = glob.glob("images/*.tif")
masks = glob.glob("masks/*.tif")

for i in range(len(images)):
    boxes = mask2bbox(images[i], masks[i])
    
    fileName = images[i].split(".")[0] + '.txt'
    file = open(fileName, "a+")
    for box in boxes:
        x_center, y_center, width, height = xywh2yoloBox(box[0], box[1], box[2], box[3])
        
        file.write('0 '+str(x_center)+' '+str(y_center)+' '+str(width)+' '+str(height)+'\n')
    file.close()
    

