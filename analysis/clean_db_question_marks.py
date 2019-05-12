#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:08:04 2019

@author: vasudharengarajan
"""

import pandas as pd

cluster_csv = "final_database.csv"
df = pd.read_csv(cluster_csv)
    
def get_pos_utterance(text):
    if "?" in text:
        #print(text.replace("?", ""))
        return text.replace("?", "")
    else:
        return text
  
df['title'] = df['title'].apply(get_pos_utterance)

output_filename = "final_database_no_question_marks.csv"
df.to_csv(output_filename)