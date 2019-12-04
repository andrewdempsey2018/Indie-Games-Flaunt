from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/action")
def action():
    return render_template("action.html")

@app.route("/puzzle")
def puzzle():
    return render_template("puzzle.html")

@app.route("/sports")
def sports():
    return render_template("sports.html")

@app.route("/educational")
def educational():
    return render_template("educational.html")