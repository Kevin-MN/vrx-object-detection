import cv2
import numpy as np


bouy_cascade = cv2.CascadeClassifier('/home/a/cascade20x20.xml')

cap = cv2.VideoCapture('/home/a/output.avi')

while True:

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bouys = bouy_cascade.detectMultiScale(gray, 1.3, 8,)   #1.3, 8 very scuffed on 20x20


    for (x, y, w, h) in bouys:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()