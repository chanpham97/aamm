from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import config
import json
import spotipy
import time
import sys
    
def get_track_features(client_id, config_id, tid):
    client_credentials_manager = SpotifyClientCredentials(client_id, config_id)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    start = time.time()
    features = sp.audio_features(tid)
    analysis = sp.audio_analysis(tid)
    delta = time.time() - start
    
    json_dump = json.dumps(features, indent=4)
    print(json_dump)
    json_features = json.loads(json_dump)
    print ("analysis retrieved in %.2f seconds" % (delta,))
    
    entry = y[0]
    return entry["energy"], entry["loudness"], entry["tempo"], entry["key"]
    

get_track_features(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET, 'spotify:track:52lJakcAPTde2UnuvEqFaK')
get_track_features(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET, 'spotify:track:0PfQd8JoZTLC7QmuSALrnH')


############# NOTES ####################
# one key feature is: energy, loudness, tempo. maybe key would allow us to classify (happy v sad for the colors)
#tid = 'spotify:track:52lJakcAPTde2UnuvEqFaK' # angry, fast, percussive, orchestral
#tid = 'spotify:track:0PfQd8JoZTLC7QmuSALrnH' # one instrument, peaceful, calm