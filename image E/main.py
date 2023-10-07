import cv2 #open cv


img = cv2.imread('white.jpg' , 0) #khandan ax sia sefid

height , width = img.shape

start_h = height // 7
start_w = width // 4
square_size = 50

img[start_h+square_size:start_h+(7*square_size) , start_w:start_w+square_size] = 0
img[start_h:start_h+square_size , start_w:start_w+(4*square_size)] = 0 
img[start_h+(3*square_size):start_h+(4*square_size) , start_w:start_w+(4*square_size)] = 0
img[start_h+(6*square_size):start_h+(7*square_size) , start_w:start_w+(4*square_size)] = 0




cv2.imwrite('result.jpg' , img) #zakhire ax

cv2.imshow('output' , img) #namayesh ax
cv2.waitKey() #zood baste nashe

