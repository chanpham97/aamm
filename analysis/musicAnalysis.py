from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import config
import json
import spotipy
import time
import math

# Reference for Spotify features: https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/

class MusicAnalyzer:
    def __init__(self, client_id, config_id):
        self.client_id = client_id
        self.config_id = config_id
    
    def scale_energy(self, energy):
        return math.ceil(energy*10.0) # 1 to 10
        
    # def scale_loudness(self, energy):
    #     if energy <= -25:
    #         return -1 # low vol
    #     if energy >= 13:
    #         return 1 # high vol
    #     else:
    #         return 0
    
    def scale_tempo(self, energy):
        if energy <= 70:
            return 1
        if energy <= 75:
            return 3
        if energy <= 80:
            return 5
        if energy <= 85:
            return 7
        if energy <= 90:
            return 9
        return 10
    
        
    def get_scaled_track_features(self, tid, annotation=None):
        #print()
        #print(tid)
        client_credentials_manager = SpotifyClientCredentials(self.client_id, self.config_id)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
        #start = time.time()
        features = sp.audio_features(tid)
        #analysis = sp.audio_analysis(tid)
        #delta = time.time() - start
        
        json_dump = json.dumps(features, indent=4)
        #print(json_dump)
        json_features = json.loads(json_dump)
        #print ("analysis retrieved in %.2f seconds" % (delta,))
        
        entry = json_features[0]
        print('energy, tempo, mode')
        print(tid, entry["energy"], entry["tempo"], entry["mode"])
        
        # if annotation:
        #     print("Annotation:", annotation)
        
        scaled_mode = 1 if entry["mode"] == 0 else 10
        return self.scale_energy(entry["energy"]), self.scale_tempo(entry["tempo"]), scaled_mode
    
def __main__():
    music_matcher = MusicAnalyzer(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET)
    
    tracks_dictionary = {
                "52lJakcAPTde2UnuvEqFaK": "Angry, fast, percussive, orchestral", 
                "0PfQd8JoZTLC7QmuSALrnH": "One instrument, peaceful, calm",
                "1LqFdwLKqa8Ep6q9LEUCih": "Two instruments, peaceful, sad",
                "2Yb67ozAhETHhy5i5eIDI1": "Happy, slow",
                "6cPbVV2I3AjhSHxB5J4Ozd": "Fast, angry",
                "2mbdpLcDqFsA5efI0LJn5i": "Fast, happy, jiggy",
                "6C5iTxvpG5Geb66InRxoSP": "Slow, happy, calm",
                "23if4cvw0UI7c8Uc5OOvss": "Happy, fast",
                "38J3F2EqXt9DnRstJiziTJ": "Gliding"

    }
    
    print("energy, tempo, mode")
    for track, annot in tracks_dictionary.items():
        print(music_matcher.get_scaled_track_features(track, annot))


__main__()

############# NOTES ####################
# one key feature is: energy, loudness, tempo. maybe key would allow us to classify (happy v sad for the colors)
#tid = 'spotify:track:52lJakcAPTde2UnuvEqFaK' # angry, fast, percussive, orchestral
#tid = 'spotify:track:0PfQd8JoZTLC7QmuSALrnH' # one instrument, peaceful, calm
 
