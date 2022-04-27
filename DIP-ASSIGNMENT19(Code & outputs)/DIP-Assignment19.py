#Laplacian filter
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
image2 = cv2.imread('jeff.JPG') # reads the image
new_image = cv2.Laplacian(image2,cv2.CV_64F)
plt.figure(figsize=(11,6))
plt.subplot(131), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(new_image, cmap='gray'),plt.title('Laplacian')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(image2 + new_image, cmap='gray'),plt.title('Resulting image')
plt.xticks([]), plt.yticks([])
plt.show()