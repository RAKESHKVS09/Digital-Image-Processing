#Assignment8:
#Task-->Read a color image & do contrast maniplution.
#display output images.
import math     #importing required libraries                                          
import numpy as np
import cv2

path = r"RAKESHKVS.jpeg" #declaring path of image
image = cv2.imread(path)                                  #Reading the image 
m,n,v = image.shape  
Increased_contrast = np.zeros(image.shape, image.dtype)
Decreased_contrast = np.zeros(image.shape, image.dtype)

alpha_1 = 1.6 # Simple contrast control for High Contrast
alpha_2 = 0.7 # Simple contrast control for Low Contrast
beta = 0    # Simple brightness control

for y in range(image.shape[0]):
    for x in range(image.shape[1]): 
        for c in range(image.shape[2]):
            Decreased_contrast[y,x,c] = np.clip(alpha_2*image[y,x,c] + beta, 0, 255) 
            Increased_contrast[y,x,c] = np.clip(alpha_1*image[y,x,c] + beta, 0, 255)

#Dispalying Images
cv2.imshow("Original",image)
cv2.imshow("Contrast Increased", Increased_contrast)
cv2.imshow("Contrast Decreased", Decreased_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()