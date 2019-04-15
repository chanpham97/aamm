from flask import Flask, flash, redirect, render_template, request, session, abort
import random
import sys
sys.path.insert(0, "../analysis/")
from musicArtMatcher import MusicArtMatcher 
import config

app = Flask(__name__)

paintings_dict = {
        "0.jpg": ["Painting with red spot", "Wassily Kandinsky", "1914"],
        "1.jpg": ["Lausanne Abstract", "Francis Picabia", "1918"],
        "2.jpg": ["Glass Painting with the Sun (Small Pleasures)", "Wassily Kandinsky", "1910"],
        "3.jpg": ["Bild no. 84", "Jacoba van Heemskerck", "1918"],
        "4.jpg": ["Spring", "David Burliuk", "1907"],
        "5.jpg": ["The Mahatmas Present Standing Point, Series II, No. 2a", "Hilma af Klint", "1920"],
        "6.jpg": ["Landscape", "Arthur Beecher Carles", "1910"],
        "7.jpg": ["Abstract Painting", "Vanessa Bell", "1914"],
        "8.jpg": ["The Yellow Curtain", "Henri Matisse", "1915"],
        "9.jpg": ["Variation", "Alexej von Jawlensky", "1918"],
        "10.jpg": ["Planar Relation", "Willi Baumeister", "1920"],
        "11.jpg": ["With full force", "Lyubov Popova", ""],
        "12.jpg": ["Eroun", "Wolfgang Paalen", "1944"],
        "13.jpg": ["1949-A-No.1", "Clyfford Still", "1949"],
        "14.jpg": ["The Air", "Joan Miro", "1937"]
}

tracks_list = [
    "52lJakcAPTde2UnuvEqFaK", "0PfQd8JoZTLC7QmuSALrnH", "1LqFdwLKqa8Ep6q9LEUCih", "2Yb67ozAhETHhy5i5eIDI1",
    "6cPbVV2I3AjhSHxB5J4Ozd", "0nF5aQoLs2YtbWwClXvumL", "2mbdpLcDqFsA5efI0LJn5i",
    "6C5iTxvpG5Geb66InRxoSP"
]

@app.route("/")
def hello():    
    painting, painting_info = random.choice(list(paintings_dict.items()))
    matcher = MusicArtMatcher(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET, 100)
    track_id = matcher.match('../app/static/images/', painting, tracks_list)
    print(track_id)
    # painting = str(painting_index % len(paintings_dict.keys())) + ".jpg"
    # painting_info = paintings_dict[painting]
    track = "https://open.spotify.com/embed/track/" + track_id
    return render_template('index.html', painting_path="/static/images/" + painting, title=painting_info[0], artist=painting_info[1], track_url=track)
 

if __name__ == "__main__":
    app.run()