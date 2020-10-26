# Course Project: Image Analysis for cancer risk assessment (8QA01)

This is a repository for the course 8QA01 at Eindhoven University of Technology. This course takes place on three platforms: Github, Canvas and Teams:

* In this Github repository you will find all content and technical part of the course
* Canvas is used for announcements, handing in your assignments, and discussion forum
* Teams is used for meetings 

Your lecturer is Veronika or Dr. Cheplygina. 

## Getting started 

In this project you will work with Python. This means you need to install software to run and edit Python code. Read more tips about getting started with Python here: https://github.com/tueimage/8qa01/blob/master/tips_code.md 

## Structure

The overall project steps can be found in the notebook (`class2020_group00_script.ipynb`), which already contains a general script to: 

* go through all the images
* measure simple features in each image
* create a plot of the measurements. 

These steps use functions, which can be find in the module `class2020_group00_functions.py`. This is where you should add more functions for completing your project, and then call these functions from the notebook. 

## Data

For the project we use images from the following paper:

Codella N, Gutman D, Celebi ME, Helba B, Marchetti MA, Dusza S, Kalloo A, Liopyris K, Mishra N, Kittler H, Halpern A. "Skin Lesion Analysis Toward Melanoma Detection: A Challenge at the 2017 International Symposium on Biomedical Imaging (ISBI), Hosted by the International Skin Imaging Collaboration (ISIC)". arXiv: 1710.05006 [cs.CV] Available: https://arxiv.org/abs/1710.05006


There are more than 2000 images in this dataset. For each image, we have the following data:

*	`ISIC_[ID].png` the image of the lesion
*	`ISIC_[ID]\_segmentation.png` the mask of the lesion, showing which pixels belong to the lesion or not
* The label of the image, i.e. whether it belongs to the Melanoma class (0 = no, 1 = yes), and/or the Keratosis class (0 = no, 1 = yes). 

The full dataset is available via https://challenge.isic-archive.com/landing/2017, but to only get the images you need, you can get the ZIP file from Surfdrive (ask your lecturer for the link).


## Intermediate assignment

Initially you will work with a subset of 100 images, which are different for each group. The format is the same as of the file `class2020_group00_id.xlsx`. One image ID corresponds to one row, and one piece of information (such as a measurement of the image) corresponds to one column. 

There are two things you need to do in your assignment, measure the images by hand, and describe your plan for the final assignment.

### Intermediate assignment - part 1

* Label your group's images by hand ("op het oog") for one or more features you plan to measure. Per feature you need to have at least three people repeating the measurements, and each person measures all 100 images. 

* For example, if you measure two features, you can have persons A, B and C measuring feature 1, and persons D, E, F measuring feature 2. Your Excel file will then have 6 additional columns.

* You can decide yourself how to measure things, but the measurement has to be numerical. For example a binary score (0 = no, 1 = yes), a scale (for example 1 to 5), etc.  

* Follow the instructions of the template and use the same format.

* Hand in the `class2020_groupXY_manual.xlsx` file on Canvas.

* This data will allow you to start doing experiments early on, so that you can spread the work inside the group. 


### Intermediate assignment - part 2

* Write down a list of features you want to measure, and the strategy you plan to use. These steps should be similar to pseudocode, for example "resize the image, subtract original image from the smaller image" etc. 

*	A possible experiment to test out your method, what could you compare with what? You could use the measurements you create, to already try this out a bit. 

* The goal of this assignment is to get feedback on your plans, there is no grade.  

* Hand in both parts of the assignment on Canvas 



## Final assignment

For the final assignment you have to hand in your report and your code, in a ZIP file. Some tips:

*	Your script/function files should be called the same as the template, only with the group number adjusted. This script has to perform everything that is necessary to create your measurements and experiments.  

*	All necessary code (except common Python packages) needs to be included in the ZIP file. 

* Do NOT include the lesion images in the ZIP file. 

*	The code has to run if it is unzipped on a different computer, after changing the directory where the images are located.


# Assessment 

Your grade is composed of 3 parts:
* 50% group work, given by your group and mentor 
* 40% report and code
* 10% presentation

The main things to pay attention to are:

*	Creativity/quality of proposed method (report/code)
*	Clarity of explanation, readability, structure of report
*	Creativity and clarity of the presentation

