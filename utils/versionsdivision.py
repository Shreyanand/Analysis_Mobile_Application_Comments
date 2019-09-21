#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:05:02 2018

@author: shrey
"""

import pickle
import datetime
from bisect import bisect

versions = {}
version_reviews = {}
with open("/Users/shrey/AnacondaProjects/Application_reviews/Experiments/ReleaseDates/RawData/version", "rb") as input_file:
    versions = pickle.load(input_file)
        
with open("/Users/shrey/AnacondaProjects/Application_reviews/Experiments/ReleaseDates/RawData/version_reviews", "rb") as input_file:
    version_reviews = pickle.load(input_file)
    
    
reviewsbyversion = {}
for key, value in versions.items():
    tempdic = {}
    for version in value:
        tempdic[version[1]] = []
    reviewsbyversion[key] = tempdic

for key,value in reviewsbyversion.items():
    breakpoints = []
    for k,v in value.items():
        breakpoints.append(k)
    breakpoints.sort()
    for review in version_reviews[key]:
        value[breakpoints[bisect(breakpoints,review[1]) - 1]].append(review)

    

#dt = []
#for key,value in reviewsbyversion.items():
#    for review in version_reviews[key]:
#        rdt = review[1]
#        dif = datetime.timedelta(10000000)
#        assver = datetime.datetime(1000,1,1,0,0,0)
#        firstver = datetime.datetime(2018,1,1,0,0,0) 
#        for k,v in value.items():
#            if firstver > k:
#                firstver = k
#            d = rdt - k
#            if d > datetime.timedelta(0):
#                if d < dif:
#                    dif = d
#                    assver = k
#        if assver == datetime.datetime(1000,1,1,0,0,0):
#            value[firstver].append(review)
#        else: 
#            value[assver].append(review)
#
count = 0                
for key,value in reviewsbyversion.items():
    for k,v in value.items():
        for review in v:
            if k - review[1] > datetime.timedelta(0):
                count += 1
print(count)
#            
           