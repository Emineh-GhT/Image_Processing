import cv2 #open cv


img = cv2.imread('4.jpg' , 0) #khandan ax sia sefid

img = cv2.resize(img , (500,500))

height , width = img.shape

threshold_value = 100
for i in range(height):
    for j in range(width):
        if img[i , j] < threshold_value:
            img[i , j] = 0
        
cv2.imwrite('result.jpg' , img) #zakhire ax

cv2.imshow('output' , img) #namayesh ax
cv2.waitKey() #zood baste nashe

