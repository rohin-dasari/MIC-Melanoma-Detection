# MIC-Melanoma-Detection


# Introduction
This project is a collaboration with the Medical Innovation Club at OSU. The main goal of this project is to develop an app that will be able to use machine learning to classify melanomas. This document will cover the basic steps of image pre-processing, image segmentation, feature extraction, and training of the neural network. The data set that was used was taken from the ISIC archive (https://www.isic-archive.com/#!/topWithHeader/wideContentTop/main). 

# Running the Program

# Image Pre-Processing
The main goal of image pre-processing is to reduce the noise, remove unnecessary parts, and enhance the image as much as possible. For noise reduction, a Gaussian blur was used. Although the Gaussian blur is not edge preserving, a small sigma value was used, which ensured that too much noise was not removed.  
