import json
from flask import Flask, render_template, redirect, url_for
import threading
from reader import readfile


# Really shit way of doing it, collects the top/new/best posts and puts them to the data.json
def getposts():
    urls = ["https://reddit.com/r/TwoSentenceHorror/new/", "https://reddit.com/r/TwoSentenceHorror/rising/", "https://www.reddit.com/r/TwoSentenceHorror/top/?t=month","https://reddit.com/r/TwoSentenceHorror/top/?t=week", "https://reddit.com/r/TwoSentenceHorror/rising/"]
    for i, url in enumerate(urls):
        print(f"Fetching {i} url(s) from {url}")
        readfile(url)

getposts()
app = Flask(__name__)

with open("data.json") as f:
    DATA = json.load(f)
    KEYS = list(DATA.keys())

current_index = 0

@app.route("/")
def index():
    global current_index
    key = KEYS[current_index]
    value = DATA[key]
    return render_template("index.html", key=key, value=value)

@app.route("/next")
def next_key():
    global current_index
    current_index = (current_index + 1) % len(KEYS)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
