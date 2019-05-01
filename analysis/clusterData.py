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

for_clustering_csv = "for_clustering.csv"
df = pd.read_csv(for_clustering_csv)

for index, row in df.iterrows():
    #print(row)
    art_info.append([row["title"], row["artistName"], row["yearAsString"], row["genre"], row["image"]])
    data.append([row["f1"], row["f2"], row["f3"], row["f4"], row["f5"], row["f6"], row["f7"], row["f8"], row["f9"]])

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
dfObj = pd.DataFrame(rows, columns = ['title' , 'artistName', 'yearAsString', 'genre', 'image', 'f1','f2','f3','f4','f5','f6','f7','f8','f9', 'label']) 
print(dfObj.head(5))

output_filename = "k_means_clustered.csv"
dfObj.to_csv(output_filename)

#kmeans.predict([[0, 0], [12, 3]])
#print(df.head(5))