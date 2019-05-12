from flask import Flask, flash, redirect, render_template, request, session, abort
import random
import csv
import sys

app = Flask(__name__)


def read_db(db_name, pairings):
    with open(db_name, "r") as in_csv:
        reader = csv.DictReader(in_csv)
        paintings = []
        for row in reader:
            paintings.append(row)
    
    with open(pairings, "r") as in_csv:
        reader = csv.DictReader(in_csv)
        pairings = {}
        for row in reader:
            pairings[row["label"]] = row["track"]

    return paintings, pairings


def get_painting(paintings):
    global pairings

    index = random.randint(0, len(paintings)-1)
    painting = paintings[index]
    title = painting["title"].decode('utf-8')
    artist = painting["artistName"].decode('utf-8')
    url = painting["image"].decode('utf-8')
    label = painting["label"]
    print index, label

    track = "https://open.spotify.com/embed/track/" + pairings[label]
    return index, title, artist, url, track


def write_feedback(file, rating):
    global view_history
    with open(file, "a+") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["track", "rating"])
        row = {"track": view_history[-1], "rating": rating}
        writer.writerow(row)


def load_page():
    global view_history
    global paintings

    index, title, artist, url, track = get_painting(paintings)
    view_history.append(index)
    print view_history
    return render_template('index.html', painting_path=url, title=title, artist=artist, track_url=track)

view_history = []
paintings, pairings = read_db("../analysis/k_means_clustered.csv", "../analysis/clusters_to_tid.csv")

@app.route("/")
def hello():   
    return load_page()

@app.route("/negative")
def negative():
    write_feedback("feedback.csv", -1)
    return load_page()


@app.route("/neutral")
def neutral():   
    write_feedback("feedback.csv", 0)
    return load_page()


@app.route("/positive")
def positive():   
    write_feedback("feedback.csv", 1)
    return load_page()


if __name__ == "__main__":
    app.run()