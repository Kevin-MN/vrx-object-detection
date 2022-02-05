import cv2


img = cv2.imread('/home/a/Downloads/bouy5050.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('/home/a/pos.jpg', img_gray)