#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:46:58 2019

@author: vasudharengarajan
"""

from sklearn.cluster import KMeans
#import numpy as np
import pandas as pd

#X = np.array([[1, 1], [2, 1], [1, 0], [4, 7], [3, 5], [3, 6]])
#
#clustering = SpectralClustering(n_clusters=2, assign_labels="discretize", random_state=0).fit(X)
#
#print(clustering.labels_)
#print(clustering)




art_info = []
data = []

#for_clustering_csv = "for_clustering.csv"
for_clustering_csv = "painting-db.csv"
df = pd.read_csv(for_clustering_csv)
df = df.fillna(0.0)

for index, row in df.iterrows():
    art_info.append([row["title"], row["artistName"], row["yearAsString"], row["genre"], row["image"]])
    
    data.append([row["brightness"], row["blockCount"], row["colorCount"], 
                 row["pink"], row["brown"], row["yellow"], row["blue"], row["gray"], row["purple"], row["black"], row["orange"], row["green"], row["white"], row["red"], 
                 row["mean_b_gradients_horiz"], row["mean_g_gradients_horiz"], row["mean_r_gradients_horiz"], row["mean_b_gradients_vert"], row["mean_g_gradients_vert"], row["mean_r_gradients_vert"] 
                 ])

k=20
kmeans = KMeans(n_clusters=k, random_state=0).fit(data)
print(k, "cluster centers: ", kmeans.cluster_centers_)
#print(len(kmeans.labels_))
#print(len(art_info))
#print(len(data))

assert(len(kmeans.labels_) == len(art_info))
assert(len(data) == len(art_info))

n = len(kmeans.labels_)

rows = []
for i in range(n):
    art_info[i].extend(data[i])
    art_info[i].append(kmeans.labels_[i])
    #print(art_info[i])
    #print(len(art_info[i]))
    rows.append(art_info[i])
    #print()
    
#Convert list of tuples to dataframe and set column names and indexes
dfObj = pd.DataFrame(rows, columns = ['title' , 'artistName', 'yearAsString', 'genre', 'image',
                                      'brightness','blockCount','colorCount',
                                      'pink','brown','yellow','blue','gray','purple', 'black', 'orange', 'green', 'white', 'red', 
                                      'mean_b_gradients_horiz', 'mean_g_gradients_horiz', 'mean_r_gradients_horiz', 'mean_b_gradients_vert', 'mean_g_gradients_vert', 'mean_r_gradients_vert',
                                      'label'
                                      ]) 

print("MADE IT")

print(dfObj.head(5))

output_filename = "k_means_clustered.csv"
dfObj.to_csv(output_filename)

#kmeans.predict([[0, 0], [12, 3]])
#print(df.head(5))