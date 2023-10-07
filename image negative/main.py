import cv2 #open cv


img1 = cv2.imread('1.jpg' , 0) #khandan ax sia sefid
img2 = cv2.imread('2.jpg' , 0) 

height1 , width1 = img1.shape
height2 , width2 = img2.shape

# for i in range(height1):
#     for j in range(width1):
#         img1[i , j] = 255 - img1[i , j] #negative
# for i in range(height2):
#     for j in range(width2):
#         img2[i , j] = 255 - img2[i , j] #negative

img1[0:height1 , 0:width1] = 255 - img1[0:height1 , 0:width1] #negative 
img2[0:height2 , 0:width2] = 255 - img2[0:height2 , 0:width2]

cv2.imwrite('result1.jpg' , img1) #zakhire ax
cv2.imwrite('result2.jpg' , img2) #zakhire ax

cv2.imshow('output' , img1) #namayesh ax
cv2.waitKey() #zood baste nashe
cv2.imshow('output' , img2) #namayesh ax
cv2.waitKey() #zood baste nashe
