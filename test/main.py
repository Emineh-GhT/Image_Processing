import cv2 #open cv


img = cv2.imread('img/one.jpg' , 0) #khandan ax sia sefid

print(img) #araye do bodi

print(img.shape) #tedad pixel ha (425*640)

height , width = img.shape
# for i in range(height):
#     for j in range(width):
#         if img[i , j] > 150:
#             img[i , j] = 255
#         elif img[i , j] <= 150:
#             img[i , j] = 0
for i in range(height):
    for j in range(width):
        img[i , j] = 255 - img[i , j] #negative

new_img = cv2.resize(img , (600,800))
print(new_img.shape)
# cv2.imshow('new' , new_img)

cv2.imwrite('result.jpg' , img) #zakhire ax

# img[0 , 0] = 255
# img[0 , 1] = 255
# img[1 , 0] = 255
# img[1 , 1] = 255
# img[0:5 , 0:5] = 255
# img[50:100 , 70:125] = 255

img[0:425 , 0:20] = 0 #samt chp qab meshki 
img[0:425 , 620:640] = 0 #samt rast qab meshki
img[0:20 , 0:640] = 0 #samt bala qab meshki 
img[405:425 , 0:640] = 0 #samt paeen qab meshki

# parvane = img[20:170 , 50:230] #joda kardn yek bakhsh
# # cv2.imshow('parvane' , parvane)
# print(parvane.shape)
# img[200:350 , 100:280] = parvane #enteqal be yekja dige


cv2.imshow('output' , img) #namayesh ax
cv2.waitKey() #zood baste nashe

