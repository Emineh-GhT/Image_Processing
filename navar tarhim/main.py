import cv2 #open cv


img = cv2.imread('janati.jpg' , 0) #khandan ax sia sefid


height , width = img.shape

cv2.line(img, (150,0), (0,100), (0,0,0), 30)

cv2.imwrite('result.jpg' , img) #zakhire ax

cv2.imshow('output' , img) #namayesh ax
cv2.waitKey() #zood baste nashe

