import cv2
import numpy as np
import os


def convert_gray_scale():
    count = 0
    for _ in np.arange(1):

        count = str(count).zfill(4)
        print(count)

        img_source = cv2.imread("/home/a/negative_images/left" + str(count) + ".jpg")
        
        img_copy = img_source.copy()
        img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
        img_resize = cv2.resize(img_gray, (100,100))
        
        cv2.imwrite("/home/a/neg_img/" + str(int(count)) + ".jpg", img_resize)

        count = int(count)
        count+=1
        count = str(count)



convert_gray_scale()