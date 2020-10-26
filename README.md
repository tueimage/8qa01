# Image analysis for cancer risk assessment (8QA01)

This is a repository for the course 8QA01 at Eindhoven University of Technology. This course takes place on three platforms: Github, Canvas and Teams:

* In this Github repository you will find all content and technical part of the course
* Canvas is used for announcements, handing in your assignments, and discussion forum
* Teams is used for meetings 

Your lecturer is Veronika or Dr. Cheplygina. 

## Project goals

In this project you will learn to measure features in images of skin lesions, and predict the diagnosis (for example, melanoma) from these features in an automatic way. You will likely:
* Study literature to find out what kind of features may be relevant for skin lesion diagnosis
* Implement methods to measure such features
* Predict the lesion diagnosis, based on the features
* Come up with experiments to test if your predictions are good
* Think about other issues concerning automatic diagnosis

## Slides 

I will explain the assignment in more detail during the lecture. The slides and recordings will be posted here after the lecture.


## Project code

In this project you will work with Python. This means you need to install software to run and edit Python code. Read more tips about getting started with Python here: https://github.com/tueimage/8qa01/blob/master/tips_code.md 

Some basis steps needed to complete the project are found in the Jupyter notebook `class2020_group00_script.ipynb`, which already contains a general script to: 

* go through all the images
* measure simple features in each image
* create a plot of the measurements
* predict the label of the image, based on the measurements

These steps use functions, which can be find in the module `class2020_group00_functions.py`. This is where you should add more functions for completing your project, and then call these functions from the notebook. 

## Data

For the project we use images from the following paper:

Codella N, Gutman D, Celebi ME, Helba B, Marchetti MA, Dusza S, Kalloo A, Liopyris K, Mishra N, Kittler H, Halpern A. "Skin Lesion Analysis Toward Melanoma Detection: A Challenge at the 2017 International Symposium on Biomedical Imaging (ISBI), Hosted by the International Skin Imaging Collaboration (ISIC)". arXiv: 1710.05006 [cs.CV] Available: https://arxiv.org/abs/1710.05006


There are more than 2000 images in this dataset. For each image, we have the following data:

*	`ISIC_[ID].png` the image of the lesion
*	`ISIC_[ID]\_segmentation.png` the mask of the lesion, showing which pixels belong to the lesion or not
* The label of the image, i.e. whether it belongs to the Melanoma class (0 = no, 1 = yes), and/or the Keratosis class (0 = no, 1 = yes). 

The full dataset is available via https://challenge.isic-archive.com/landing/2017, but to only get the images you need, you can also get it here: https://surfdrive.surf.nl/files/index.php/s/ZxuiojXx8rmIq3q 


## Assignments

This project consists of two assignments and a presentation:

* Intermediate assignment, which is NOT graded, but for which you will get feedback. For this assignment you need to think of some image features you want to measure, and label a number of images. You hand in a ZIP file on Canvas, with a short report and an Excel sheet with labels. More details here: https://github.com/tueimage/8qa01/blob/master/tips_assignment_intermediate.md

* Final assignment, which is graded. You hand in a ZIP file on Canvas, with your report and code. More details here: https://github.com/tueimage/8qa01/blob/master/tips_assignment_final.md

* The final assignment is also concluded with a "presentation", which is a YouTube movie of 3 minutes. 

