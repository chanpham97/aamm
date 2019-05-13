#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:45:24 2019

@author: vasudharengarajan
"""

import setup
import colorAnalysis
import pandas as pd

MAX_VAL = 300

def get_knn_classifier_and_accuracy(database_path):
    df = pd.read_csv(database_path)
    X = df.drop(['Unnamed: 0','title','artistName','yearAsString','genre','image','label'], axis=1)
    y = df.label
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    
    return knn, knn.score(X_test, y_test), list(X.columns)

def get_vector_dict_for_image(image_path):

    img_bgr = colorAnalysis.read_bgr(image_path)
    img_bgr = colorAnalysis.resize_image(img_bgr, MAX_VAL) if MAX_VAL else colorAnalysis.resize_image(img_bgr)
    return setup.form_vector(colorAnalysis.ColorAnalysis(), img_bgr)

def get_prediction_for_image(image_path):
    art_vector_dict = get_vector_dict_for_image(image_path)
    
    knn, acc, col_list = get_knn_classifier_and_accuracy("final_database.csv")

    list_to_predict = []
    for header in col_list:
        list_to_predict.append(art_vector_dict[header])
        
    return knn.predict([list_to_predict])[0]

# print(get_prediction_for_image("Kandinsky_Wassily.Landscape_with_red_spots.1913.jpg"))

