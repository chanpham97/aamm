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
    
    def match(self,  art_filename, track_list):
        img_bgr = cv.imread(art_filename, cv.IMREAD_COLOR)
        img_bgr = colorAnalysis.resize_image(img_bgr, self.max_val) if self.max_val else colorAnalysis.resize_image(img_bgr)
        
        color_sentiment, num_colors, brightness = (colorAnalysis.get_scaled_values(img_bgr))
        target_music_vector = self.convert_art_to_music_vector(color_sentiment, num_colors, brightness)
        
        musicAnalyzer = MusicAnalyzer(self.client_id, self.config_id)
        
        closest_track_tid = ""
        closest_distance = sys.maxsize
        for track in track_list:
            energy_loudness_tempo_key = musicAnalyzer.get_scaled_track_features(track)
            dist = distance.euclidean(target_music_vector, energy_loudness_tempo_key)
            #print(target_music_vector)
            #print(energy_loudness_tempo_key)
            #print(dist)
            if dist < closest_distance:
                closest_distance = dist
                closest_track_tid = track
            if dist == closest_distance and closest_track_tid != "":
                closest_track_tid = random.choice([closest_track_tid, track])
        
        return closest_track_tid
            
            
    def convert_art_to_music_vector(self, color_sentiment, num_colors, brightness):
        if color_sentiment < 0:
             key = 0
        tempo = num_colors
        loudness = num_colors
        energy = brightness
        return energy, loudness, tempo, key
        
def __main__():
    
    track_list = [
            "spotify:track:52lJakcAPTde2UnuvEqFaK", 
            "spotify:track:0PfQd8JoZTLC7QmuSALrnH"]
    art_filename = sys.argv[1]
    
    matcher = MusicArtMatcher(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET, 300)
    
    print("RESULT:" , matcher.match(art_filename, track_list))
    
__main__()