#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:04:56 2019

@author: vasudharengarajan
"""

import pandas as pd

paintings_info_csv_filename = "paintings-info.csv"
df = pd.read_csv(paintings_info_csv_filename)

def remove_brackets(s):
    s = s.replace("[", "")
    s = s.replace("]", "")
    return s

df['no_brackets'] = df['vector'].apply(remove_brackets)
df[['f1','f2','f3','f4','f5','f6','f7','f8','f9']] = df.no_brackets.str.split(",",expand=True,)

df_for_csv = df.drop(['vector', 'no_brackets'], axis=1)
print(df_for_csv.head(10))

output_filename = "for_clustering.csv"
df_for_csv.to_csv(output_filename)