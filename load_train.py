# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 00:47:05 2018

@author: Divyang Arora
"""
from __future__ import print_function
from PIL import Image
import os
import numpy as np

# =============================================================================
def crop(image):
    width,height = image.size
    left = (width-512)/2
    top = (height-512)/2
    right = (width+512)/2
    bottom = (height+512)/2
    image = image.crop((left,top,right,bottom))
    return image

path = 'I:/train'
train_labels1 = os.listdir(path)
train_labels = ['MotoX','HTC-1-M7','iP4s','GalaxyN3','MotoNex6','LG5x','Nex7','GalaxyS4','MotoMax','ip6']


i = 0
j = 7
while j < 10:
    imgs = Image.open('I:/train/'+ train_labels1[j]+'/('+ train_labels[j] + ')1.jpg').convert('RGB') #empty dummy array, we will append to this array all the images
    imgs = crop(imgs)
    imgs = np.array(imgs)
    directory_name = 'I:/train/' + train_labels1[j]+'/'
    for filename in os.listdir(directory_name):    
        if filename != '(' + train_labels[j] + ')1.jpg' :
            print(filename+str(i))    
            img = Image.open(os.path.join(directory_name,filename)).convert('RGB')
            img = crop(img)
            imgs = np.append(imgs, np.array(img), axis=0) #
        i = i+1
    imgs = imgs.reshape(275,512,512,3)
    print('Saving as a .npy file')
    np.save("E:/DataSets/CameraModel/train_image"+str(j)+".npy",imgs)    
    i = 0
    j  = j + 1

