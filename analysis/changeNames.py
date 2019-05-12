#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:33:41 2019

@author: vasudharengarajan
"""

import pandas as pd
import json

cluster_csv = "k_means_clustered.csv"
df = pd.read_csv(cluster_csv)


    
def get_pos_utterance(text):
    with open("artists-all.json", "r", encoding="utf-8") as f:
        arr = json.load(f)
        #print(len(arr))
        for i in range(len(arr)):
            val = arr[i]
            artistName = val['artistName']
            lastNameFirst = val['lastNameFirst']
            if text == lastNameFirst:
                #print(text, " to ", artistName)
                return artistName
    print("***********",text,"*************")
    return text
  
df['artistName'] = df['artistName'].apply(get_pos_utterance)

output_filename = "fixed_names.csv"
df.to_csv(output_filename)