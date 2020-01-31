# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:28:41 2020

@author: AGB90

Take .csv data and perform moving centered average over range x
"""
#import relevant libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
#import sys
#import math

#set directory
os.chdir('path')

#file to smooth
filename ='noisy_XRD_data.csv'

#data cleaning
xrd_data = pd.read_csv(filename, skiprows = 25, skipfooter = 3, engine = 'python') #engine = 'python' when using skipfooter

#print xrd_data.head()

#data cleaning 2
new_data = xrd_data.drop(xrd_data.columns[[1]], axis = 1)

#print new_data.head()

#select relevant x y cols
theta_angle = new_data.iloc[:,0]
intensity = new_data.iloc[:,1]

#plot cols (original data)
plt.plot(theta_angle, intensity, color = 'b')

#smothing parameters
av_no = 10
start_no = 0

#initialise smoothing dataframes
theta_smooth =[]
intensity_smooth = []

#for loops to average over set range
for number in theta_angle: #summing 2theta data
    avg_2theta = np.mean(theta_angle[start_no:av_no + start_no])
    theta_smooth.append(avg_2theta)
    start_no +=1

#reinitialise smoothing parameters - fix this
av_no = 10
start_no = 0
    
for number in intensity: #summing intensity data
    avg_intensity = np.mean(intensity[start_no:av_no + start_no])
    intensity_smooth.append(avg_intensity)
    start_no +=1

#plot results
plt.plot(theta_smooth, intensity_smooth, color = 'r')

#concatenate lists
smooth_XRD = zip(theta_smooth, intensity_smooth)
