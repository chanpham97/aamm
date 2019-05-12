#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:12:01 2019

@author: vasudharengarajan
"""
import pandas as pd
import urllib.request as req
import os
import glob
import math

paintings_info_csv_filename = "k_means_clustered.csv"
k = 20

df = pd.read_csv(paintings_info_csv_filename)

print("Deleted files:")
for i in range(0,k):
    path = 'clusters/'+str(i)+'/*'
    files = glob.glob(path)
    
    for f in files:
        os.remove(f)
    print(files)

print()
print("All removed!")
print()
print("Downloading images grouped by cluster...")

for index, row in df.iterrows():
    imgurl = str(row["image"])
    artistName = row["artistName"].replace(" ", "_")
    title = row["title"].replace(" ", "_")
    
    #print(type(row["yearAsString"]))
    #print(row["yearAsString"])
    
    if math.isnan(row["yearAsString"]):
        yearAsString = "Year_unknown"
    else: 
        yearAsString = str(int(row["yearAsString"]))
    
    filename = artistName+"."+title+"."+yearAsString+".jpg"
    print(filename)
    req.urlretrieve(imgurl, "clusters/"+str(row["label"])+"/"+filename)

print("Download finished.")
