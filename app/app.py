from flask import Flask, flash, redirect, render_template, request, session, abort
import random
app = Flask(__name__)
 
@app.route("/")
def hello():
    paintings_dict = {
        "1.jpg": ["Lausanne Abstract", "Francis Picabia", "1918"],
        "2.jpg": ["Glass Painting with the Sun (Small Pleasures)", "Wassily Kandinsky", "1910"]}
    painting, painting_info = random.choice(list(paintings_dict.items()))
    track = "https://open.spotify.com/embed/track/2XKFnwB6djxrJCjR3PdeRb?si=SfXkZ-koQ-e8uW8FiCo8tA"
    return render_template('index.html', painting_path="/static/images/" + painting, title=painting_info[0], artist=painting_info[1], track_url=track)
 
if __name__ == "__main__":
    app.run()