from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

#Connect to the database that holds the games information

app.config["MONGO_DBNAME"] = "indie_flaunt"

#note remove this (username&password) and use env variable instead

app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@andrewcluster-igjjx.mongodb.net/indie_flaunt?retryWrites=true&w=majority"

#make an instance of PyMongo and pass the app in
mongo = PyMongo(app)

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

@app.route("/get_games")
def get_games():
    return render_template("test.html", games = mongo.db.games.find())