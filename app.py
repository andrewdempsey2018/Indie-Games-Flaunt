from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to the database that holds the games information
app.config["MONGO_DBNAME"] = "indie_flaunt"

# note remove this (username&password) and use env variable instead
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@andrewcluster-igjjx.mongodb.net/indie_flaunt?retryWrites=true&w=majority"

# make an instance of PyMongo and pass the app in
mongo = PyMongo(app)

# get a list of all the games currently in the database
@app.route("/")
@app.route("/get_games")
def get_games():
    return render_template("games.html", games = mongo.db.games.find())

# open up the share game page
@app.route("/share_game")
def share_game():
    return render_template("share.html", games = mongo.db.games.find())

# add a game to the database
@app.route("/add_game", methods=["POST"])
def add_game():
    games2=mongo.db.games
    games2.insert_one(request.form.to_dict())
    return redirect(url_for('get_games'))