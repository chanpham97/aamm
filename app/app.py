from flask import Flask, flash, redirect, render_template, request, session, abort
import random
import csv
import sys
# sys.path.insert(0, "../analysis/")
# from musicArtMatcher import MusicArtMatcher 
# import config

app = Flask(__name__)


def read_db(db_name):
    with open(db_name, mode="r") as in_csv:
        reader = csv.DictReader(in_csv)
        paintings = []
        for row in reader:
            paintings.append(row)
    return paintings


def get_painting(paintings):
    index = random.randint(0, len(paintings)-1)
    print index
    painting = paintings[index]
    title = painting["title"].decode('utf-8')
    artist = painting["artistName"].decode('utf-8')
    url = painting["image"].decode('utf-8')
    
    track_id = '52lJakcAPTde2UnuvEqFaK'
    track = "https://open.spotify.com/embed/track/" + track_id
    return index, title, artist, url, track


view_history = []
tracks_list = [
    "52lJakcAPTde2UnuvEqFaK", "0PfQd8JoZTLC7QmuSALrnH", "1LqFdwLKqa8Ep6q9LEUCih", "2Yb67ozAhETHhy5i5eIDI1",
    "6cPbVV2I3AjhSHxB5J4Ozd", "0nF5aQoLs2YtbWwClXvumL", "2mbdpLcDqFsA5efI0LJn5i", "0Cr1H8kCXN5qBAQCHYtVGu",
    "6qxFruTA3sBLF29FXLR6LW", "7iocNjLrxPHLl8njgRlv5U", #"4cKmnSLAhwxaWKXQhfz5Ju"
]
paintings = read_db("painting-db.csv")

@app.route("/")
def hello():   
    global view_history
    global paintings
    
    index, title, artist, url, track = get_painting(paintings)
    view_history.append(index)
    print view_history
    return render_template('index.html', painting_path=url, title=title, artist=artist, track_url=track)
 
# @app.route("/prev")
# def previous():
#     print painting_index
#     painting, painting_info, track = get_dependencies() 
#     return render_template('index.html', painting_path="/static/images/" + painting, title=painting_info[0], artist=painting_info[1], track_url=track)

# @app.route("/next")
# def next():
#     global painting_index
#     painting_index = (painting_index + 1) % len(paintings_dict.keys())
#     print painting_index
#     painting, painting_info, track = get_dependencies() 
#     return render_template('index.html', painting_path="/static/images/" + painting, title=painting_info[0], artist=painting_info[1], track_url=track)


if __name__ == "__main__":
    app.run()