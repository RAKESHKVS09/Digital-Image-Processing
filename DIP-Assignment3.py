#**********************Assignment3***************************
#Task: Create two images one with a white circle at center and another with a white rentangle at center and perform all logical gate operations on both images and display the output images. 

import math                                  #importing required libraries.
import numpy as np
import cv2

Img1 = np.zeros((512,512),np.uint8)         #declaring two black images to do operations.
Img2 = np.zeros((512,512),np.uint8)

Img1 = cv2.circle(Img1,(235,250),80,(255,255,255),-1)            
Img2 = cv2.rectangle(Img2,(100,300),(330,190),(255,255,255),-1) #Making a white circle and rectangle at center of two images respectively


#performing all logic gates operations and displaying the output images

cv2.imshow("white rectangle at center image",Img2)
cv2.waitKey(0)
cv2.imshow("white circle at center image",Img1)
cv2.waitKey(0)
cv2.imshow("AND operation",cv2.bitwise_and(Img1,Img2))
cv2.waitKey(0)
cv2.imshow("NAND operation",cv2.bitwise_not(cv2.bitwise_and(Img1,Img2)))
cv2.waitKey(0)
cv2.imshow("OR operation",cv2.bitwise_or(Img1,Img2))
cv2.waitKey(0)
cv2.imshow("NOR operation",cv2.bitwise_not(cv2.bitwise_or(Img1,Img2)))
cv2.waitKey(0)
cv2.imshow("EXOR operation",cv2.bitwise_xor(Img1,Img2))
cv2.waitKey(0)
cv2.imshow("EXNOR operation",cv2.bitwise_not(cv2.bitwise_xor(Img1,Img2)))
cv2.waitKey(0)