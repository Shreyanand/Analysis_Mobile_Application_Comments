#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 14:39:36 2018

@author: shrey
"""
import mysql.connector 
import pickle

# open connection to the database  
conn =  mysql.connector.connect(host='yangtze.csc.ncsu.edu',  
                       port=3306,  
                       user='appreview',  
                       passwd='mas!321',  
                       db='app_reviews',  
                       charset='utf8')  
cursor = conn.cursor(buffered=True)  

versions = {}

sql = "SELECT * FROM releases"  
cursor.execute(sql)  
for (version, date, content, appId) in cursor:
    if appId in versions:
        versions[appId].append([version,date])
    else:
        versions[appId] = [[version,date]]
# close connection to the database  

with open("/Users/shrey/AnacondaProjects/Application_reviews/Experiments/ReleaseDates/RawData/version", "wb") as output_file:
    pickle.dump(versions, output_file)

version_reviews = {}
#version_reviews["566635048"] = []
#sql = "SELECT * FROM reviews WHERE appID = " + "566635048"
#cursor.execute(sql) 
#for (cid,title,body,rating,user,appName,appId,date,customerType,voteCount,voteSum) in cursor:
#    version_reviews[appId].append([title + body,date])
for appId in versions:
    version_reviews[appId] = []
    sql = "SELECT * FROM reviews WHERE appID = " + appId
    cursor.execute(sql) 
    for (cid,title,body,rating,user,appName,appId,date,customerType,voteCount,voteSum) in cursor:
        version_reviews[appId].append([title + body,date])
        
with open("/Users/shrey/AnacondaProjects/Application_reviews/Experiments/ReleaseDates/RawData/version_reviews", "wb") as output_file:
    pickle.dump(version_reviews, output_file)
        
cursor.close()  
conn.close()
