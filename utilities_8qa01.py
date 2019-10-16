"""
Main module for 8QA01 code
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from skimage import morphology


def scatter_data(X1, X2, Y, ax=None):
    # scatter_data displays a scatterplot of dataset X1 vs X2, and gives each point
    # a different color based on its label in Y

    class_labels, indices1, indices2 = np.unique(Y, return_index=True, return_inverse=True)
    if ax is None:
        fig = plt.figure(figsize=(8,8))
        ax = fig.add_subplot(111)
        ax.grid()

    colors = cm.rainbow(np.linspace(0, 1, len(class_labels)))
    for i, c in zip(np.arange(len(class_labels)), colors):
        idx2 = indices2 == class_labels[i]
        lbl = 'Class '+str(i)
        ax.scatter(X1[idx2], X2[idx2], color=c, label=lbl)

    return ax


def measureAreaPerimeter(maskImage):

    #Measure area: the sum of all white pixels in the mask image
    area = np.sum(maskImage)

    #Measure perimeter: first find which pixels belong to the perimeter.
    struct_el = morphology.disk(1)
    maskEroded = morphology.binary_erosion(maskImage, struct_el)
    perimeterImage = maskImage - maskEroded

    #Now we have the perimeter image, the sum of all white pixels in it
    perimeter = np.sum(perimeterImage)

    return area, perimeter
