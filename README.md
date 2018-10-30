# Camera-Model-Identification
## Objective:  
To build a model which is able to identify the source of the image dataset (i.e. the camera model). 
## Dataset:  
The dataset contains of 2750 training images from 10 different camera models (classes) along with 2640 test images. Some of the test images are manipulated using different technique like JPEG compression, bicubic interpolation and gamma correction. 
10 classes:
1.HTC-1-M7
2.iPhone-4s
3.iPhone-6
4.LG-Nexus-5x
5.Motorola-Droid-Maxx
6.Motorola-Nexus-6
7.Motorola-X
8.Samsung-Galaxy-Note3
9.Samsung-Galaxy-S4
10.Sony-NEX-7
## Methodology:
1.	Cropping training images to a fixed size of 512*512 and loading the training images.
2.	Splitting the test images into 2 categories : Manipulated and Unaltered and loading it.
3.	Building a model/architecture which trains on the training dataset.
4.	Restoring the manipulated images.
5.	Combining the unaltered and restored images into the test set.
6.	Find the predicted labels.
Link of the Kaggle competition: https://www.kaggle.com/c/sp-society-camera-model-identification
# Current Status: 
Model trained with over 90 % training as well as validation accuracy. 
