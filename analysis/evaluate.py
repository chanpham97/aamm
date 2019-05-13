#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:05:11 2019

@author: vasudharengarajan
"""

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

cluster_csv = "feedback.csv"
df = pd.read_csv(cluster_csv, usecols=[0,1], names=['index', 'grade'])

db_csv = "final_database.csv"
other = pd.read_csv(db_csv)

#print(other["Unnamed: 0"].head(5))

df_new = df.join(other, on='index', how='left')
#print(df_new.head(5))

#print(df_new["label"].head(5))
#print(df_new["grade"].head(5))

dic = {}
for index, row in df_new.iterrows():
    cluster = row["label"]
    grade = row["grade"]
    if cluster not in dic:
        dic[cluster] = [grade]
    else:
        dic[cluster].append(grade)

keys = sorted(list(dic.keys()))
all_keys = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
print()
print("Clusters represented: ", keys)
print("Number of clusters represented: ", len(keys))
print()
print("Clusters missed: ", set(all_keys) - set(keys))
print("Number of clusters missed: ", len(set(all_keys) - set(keys)))
print()

print("*************************************")

print()
total_counts = Counter(list(df_new["grade"]))
print("Total", ": ", total_counts)

plt.bar(list(total_counts.keys()), total_counts.values())
plt.show()

for key in sorted(dic.keys()):
    cluster_counts = Counter(dic[key])
    print("Cluster ", key, ": ", cluster_counts)
    plt.bar(list(cluster_counts.keys()), cluster_counts.values())
    plt.show()

print("*************************************")
print()

print("Total", ": ", total_counts)
total_counts_percent_list = [(i, round( (total_counts[i] / len(list(df_new["grade"]))), 2)) for i in total_counts]
print("In percentage", ": ", total_counts_percent_list)
print()

for key in sorted(dic.keys()):
    cluster_counts = Counter(dic[key])
    print("Cluster ", key, ": ", cluster_counts)
    #cluster_counts_percent_list = [(i, cluster_counts[i] / len(dic[key])) for i in cluster_counts]
    #print("In percentage:")
    #print(cluster_counts_percent_list)
    #print()
print()
for key in sorted(dic.keys()):
    cluster_counts = Counter(dic[key])
    #print("Cluster ", key, ": ", cluster_counts)
    cluster_counts_percent_list = [(i, round( (cluster_counts[i] / len(dic[key])), 2)) for i in cluster_counts]
    print("Cluster ", key, ": ", cluster_counts_percent_list)
    #print()

print()    
print("*************************************")
