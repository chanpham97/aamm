#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:29:40 2019

@author: vasudharengarajan
"""

import colorAnalysis
from musicAnalysis import MusicAnalyzer
import cv2 as cv
import sys
import config
from scipy.spatial import distance
import random

class MusicArtMatcher:
    def __init__(self, client_id, config_id, max_dimension_art):
        self.client_id = client_id
        self.config_id = config_id
        self.max_val = max_dimension_art
    
    def match(self,  file_path, art_filename, track_list):
        img_bgr = cv.imread(file_path + art_filename, cv.IMREAD_COLOR)
        if img_bgr is None:
            print("not read")
            return
        img_bgr = colorAnalysis.resize_image(img_bgr, self.max_val) if self.max_val else colorAnalysis.resize_image(img_bgr)
        color_sentiment, scaled_num_colors, scaled_brightness = (colorAnalysis.get_scaled_values(img_bgr))
        print('sentiment, number of colors, brightness')
        print('color scaled', color_sentiment, scaled_num_colors, scaled_brightness)
        target_music_vector = self.convert_art_to_music_vector(color_sentiment, scaled_num_colors, scaled_brightness)
        
        musicAnalyzer = MusicAnalyzer(self.client_id, self.config_id)
        
        closest_track_tid = ""
        closest_distance = sys.maxsize
        closest_tracks = []
        for track in track_list:
            energy_tempo_key = musicAnalyzer.get_scaled_track_features(track)
            dist = distance.euclidean(target_music_vector, energy_tempo_key)
            # print()
            # print("target vactor: ", target_music_vector)
            # print("track vector: ", energy_tempo_key)
            # print("distance: ", dist)
            if dist < closest_distance:
                closest_tracks = []
                closest_distance = dist
                closest_track_tid = track
                closest_tracks.append(track)
            if dist == closest_distance and closest_track_tid != "":
                closest_track_tid = random.choice([closest_track_tid, track])
                closest_tracks.append(track)
        
        print('same', closest_tracks)
        return closest_track_tid
            
            
    def convert_art_to_music_vector(self, color_sentiment, scaled_num_colors, scaled_brightness):
        key = 1 if color_sentiment < 5 else 10
        energy = scaled_num_colors
        #loudness = num_colors
        tempo = scaled_brightness
        return energy, tempo, key
        
def __main__():
    tracks_dictionary = {
        "52lJakcAPTde2UnuvEqFaK", "0PfQd8JoZTLC7QmuSALrnH", "1LqFdwLKqa8Ep6q9LEUCih",
        "2Yb67ozAhETHhy5i5eIDI1", "6cPbVV2I3AjhSHxB5J4Ozd", "2mbdpLcDqFsA5efI0LJn5i",
        "6C5iTxvpG5Geb66InRxoSP", "23if4cvw0UI7c8Uc5OOvss","38J3F2EqXt9DnRstJiziTJ"
    }
    art_filename = sys.argv[1]
    
    matcher = MusicArtMatcher(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET, 300)
    
    print("RESULT:" , matcher.match('', art_filename, track_list))
    
# __main__()