from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import config
import json
import spotipy
import time

class MusicMatcher:
    def __init__(self, client_id, config_id):
        self.client_id = client_id
        self.config_id = config_id
    
    def scale_energy(self, energy):
        if energy <= 0.05:
            return -1 # low energy
        if energy >= 0.4:
            return 1 # high energy
        else:
            return 0
        
    def scale_loudness(self, energy):
        if energy <= -25:
            return -1 # low energy
        if energy >= 13:
            return 1 # high energy
        else:
            return 0
    
    def scale_tempo(self, energy):
        if energy <= 40:
            return -1 # low energy
        if energy >= 80:
            return 1 # high energy
        else:
            return 0
        
    def get_scaled_track_features(self, tid, annotation=None):
        print()
        print(tid)
        client_credentials_manager = SpotifyClientCredentials(self.client_id, self.config_id)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
        start = time.time()
        features = sp.audio_features(tid)
        #analysis = sp.audio_analysis(tid)
        #delta = time.time() - start
        
        json_dump = json.dumps(features, indent=4)
        #print(json_dump)
        json_features = json.loads(json_dump)
        #print ("analysis retrieved in %.2f seconds" % (delta,))
        
        entry = json_features[0]
        print(entry["energy"], entry["loudness"], entry["tempo"], entry["mode"])
        
        if annotation:
            print("Annotation:", annotation)
            
        return self.scale_energy(entry["energy"]), scale_loudness(entry["loudness"]), scale_tempo(entry["tempo"]), entry["mode"]
    
def __main__():
    music_matcher = MusicMatcher(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET)
    
    tracks_dictionary = {
                "spotify:track:52lJakcAPTde2UnuvEqFaK": "Angry, fast, percussive, orchestral", 
                "spotify:track:0PfQd8JoZTLC7QmuSALrnH": "One instrument, peaceful, calm"
             }
    
    for track,annot in tracks_dictionary.items():
        print(music_matcher.get_scaled_track_features(track, annot))

__main__()

############# NOTES ####################
# one key feature is: energy, loudness, tempo. maybe key would allow us to classify (happy v sad for the colors)
#tid = 'spotify:track:52lJakcAPTde2UnuvEqFaK' # angry, fast, percussive, orchestral
#tid = 'spotify:track:0PfQd8JoZTLC7QmuSALrnH' # one instrument, peaceful, calm
 
