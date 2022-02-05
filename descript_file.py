import cv2
import numpy as np
import os

def create_pos_and_neg():
    for file_type in ['/home/a/neg']:

        for img in os.listdir(file_type):
            if file_type == '/home/a/neg':
                line = 'neg/'+img+'\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)
                    print(line)





create_pos_and_neg()