import numpy as np
import cv2 #open cv


img = cv2.imread('white.jpg' , 0) #khandan ax sia sefid

print(img) #araye do bodi

height , width = img.shape

for i in range(height):
    intensity = int(i / height * 255)
    img[i, :] = intensity

img = np.flipud(np.fliplr(img)) #rotate ax

cv2.imwrite('result.jpg' , img) #zakhire ax

cv2.imshow('output' , img) #namayesh ax
cv2.waitKey() #zood baste nashe

