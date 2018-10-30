# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 01:47:53 2018

@author: Dell
"""


import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

test_path = 'F:/test/'

x_test = []
counts = 0
data_number = 0
test_type_code = np.zeros(2640)
print('Inputing Dataset')
for filename in os.listdir(test_path):
    print(filename)
    X = np.array(Image.open(test_path + filename))
    x_test.append(X)
    test_type = filename.split('_')[2].split('.')[0]
    if (test_type == 'manip'):
        test_type_code[data_number*264+counts] = 1
    counts += 1
    print(counts)
    print(data_number+1)
    if counts==264:
        print('Saving as a .npy file')
        counts = 0
        data_number += 1
        x_test = np.array(x_test)
        np.save("F:/test_image_data"+str(data_number)+".npy",x_test)
        print('Reseting x_test and y_test')
        x_test = []
    else:
        continue
np.save('F:/test_type.npy',test_type_code)
print('END')