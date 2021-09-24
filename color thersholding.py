# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:15:19 2021

@author: dell
"""
import numpy as np
import cv2 as cv

i,j=0,0

#captures the video from web cam0
cap = cv.VideoCapture(0)
#to check camera if open or not
if not cap.isOpened():
    print("Cannot open camera")
    exit()
# It create a img or frame for pad output    
img = np.zeros((512,512,3), np.uint8)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # setting upper and lower limit for color thresholding
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    #this detect the only the cap or stylus
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    
    #coutours is calculated to find centroid of stylus
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cv.drawContours(frame, contours, -1, (0,255,0), 3)
    
    if contours and cv.contourArea(max(contours,key=cv.contourArea)):
        c=max(contours,key=cv.contourArea)
        M=cv.moments(c)
        #x1 and y1 are coordinated of centroid
        x1=int(M['m10']/M['m00'])
        y1=int(M['m01']/M['m00'])
        
        # for value of i,j=, this will assign it a new value and at this frame drawing does not occurs
        if i==0 and j==0:
            i,j=x1,y1
        else:
            cv.line(img,(i,j),(x1,y1),(255,0,0),5)
            i,j=x1,y1
            #lines are drawn for a smooth output 
    else:
        i,j=0,0
        # if coutour is not detected i,j=, will again be equal 0 , this will give us a perfect output
    
    #The frames and PAD is displayed to user 
    cv.imshow('PAD SCREEN',frame)
    cv.imshow('VIRTUAL PAD',img)
    #user need to press 'q' to quit vertual pad
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
