from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to the database that holds the games information
app.config["MONGO_DBNAME"] = "IGF_DB"

# note remove this (username&password) and use env variable instead
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@andrewcluster-igjjx.mongodb.net/IGF_DB?retryWrites=true&w=majority"

# make an instance of PyMongo and pass the app in
mongo = PyMongo(app)

# get a list of all the games currently in the database
@app.route("/")
@app.route("/get_games")
def get_games():
    return render_template("games.html", games = mongo.db.IGF_COLL.find())

# open up the share game page
@app.route("/share_game")
def share_game():
    return render_template("share.html", games = mongo.db.IGF_COLL.find())

# open up the action games page
@app.route("/action")
def action():
    return render_template("action.html", games = mongo.db.IGF_COLL.find())

# action / sports / puzzle / educational pages seperated should be one page - issue with duplicate code
@app.route("/sports")
def sports():
    return render_template("sports.html", games = mongo.db.IGF_COLL.find())

@app.route("/educational")
def educational():
    return render_template("educational.html", games = mongo.db.IGF_COLL.find())

@app.route("/puzzle")
def puzzle():
    return render_template("puzzle.html", games = mongo.db.IGF_COLL.find())

# open up the dedicated game page (page that features one game in full)
# gameName was passed from games.html. We search our database and pick this one game, then pass it to "dedicated.html"
@app.route("/dedicated")
def dedicated():
    gameName = request.args.get('gameName', None)
    return render_template("dedicated.html", game = mongo.db.IGF_COLL.find_one({ 'title': gameName }))

@app.route("/edit")
def edit():
    gameName = request.args.get('gameName', None)
    return render_template("edit.html", game = mongo.db.IGF_COLL.find_one({ 'title': gameName }))

# add a game to the database
@app.route("/add_game", methods=["POST"])
def add_game():
    games=mongo.db.IGF_COLL
    games.insert_one(request.form.to_dict())
    return redirect(url_for('get_games'))