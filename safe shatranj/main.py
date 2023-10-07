import cv2

image = cv2.imread('white.png' , 0)

image = cv2.resize(image , (800,800))

height , width = image.shape

# اندازه هر خانه شطرنج
square_size = width // 8

# رسم خانه‌های سیاه و سفید
for i in range(8):
    for j in range(8):
        x, y = j * square_size, i * square_size
        if (i + j) % 2 == 0:
            image[y:y+square_size, x:x+square_size] = 0

cv2.imwrite('result.jpg' , image) #zakhire ax

cv2.imshow('output' , image) #namayesh ax
cv2.waitKey() #zood baste nashe
