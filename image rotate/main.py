import numpy as np
import cv2 #open cv


img = cv2.imread('3.jpg' , 0) #khandan ax sia sefid

# # چرخاندن تصویر 180 درجه
# img = cv2.rotate(img, cv2.ROTATE_180)

img = np.flipud(np.fliplr(img)) #rotate ax

cv2.imwrite('result.jpg' , img) #zakhire ax

cv2.imshow('output' , img) #namayesh ax
cv2.waitKey() #zood baste nashe

