from flask import Flask, flash, redirect, render_template, request, session, abort
import random
app = Flask(__name__)
 
@app.route("/")
def hello():
    paintings = ["https://uploads0.wikiart.org/images/wassily-kandinsky/glass-painting-with-the-sun-small-pleasures-1910.jpg!Blog.jpg", "https://uploads6.wikiart.org/images/wassily-kandinsky/untitled.jpg!Large.jpg", "https://uploads4.wikiart.org/images/francis-picabia/lausanne-abstract.jpg!Large.jpg"]
    painting = paintings[random.randint(0, len(paintings)-1)]
    track = "https://open.spotify.com/embed/album/1DFixLWuPkv3KT3TnV35m3"
    return render_template('index.html', painting_url=painting, track_url=track)
 
if __name__ == "__main__":
    app.run()