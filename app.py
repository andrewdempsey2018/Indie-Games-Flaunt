from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
# ObjectId to cast identifiers to the correct format for Mongo
from bson.objectid import ObjectId
# needed for implementation of random game feature
from random import randint

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
    gameId = request.args.get('gameId', None)
    return render_template("dedicated.html", game=mongo.db.IGF_COLL.find_one({ '_id': ObjectId(gameId) }))

# Edit task
@app.route("/edit")
def edit():
    gameId=request.args.get('gameId', None)
    return render_template("edit.html", game=mongo.db.IGF_COLL.find_one({ '_id': ObjectId(gameId) }))

@app.route('/update_game', methods=["POST"])
def update_game():
    gameId=request.args.get('gameId', None)
    games = mongo.db.IGF_COLL
    games.update( {'_id': ObjectId(gameId)},
    {
        'title':request.form.get('title'),
        'genre':request.form.get('genre'),
        'developer':request.form.get('developer'),
        'link': request.form.get('link'),
        'shortDescription':request.form.get('shortDescription'),
        'description':request.form.get('description'),
        'screenshot1':request.form.get('screenshot1'),
        'screenshot2':request.form.get('screenshot2'),
        'screenshot3':request.form.get('screenshot3')
    })
    return redirect(url_for('get_games'))

# used gameId passed from "dedicated" game page. Call the remove menthod then redirect to main page
@app.route("/delete_game")
def delete_game():
    gameId=request.args.get("gameId", None)
    mongo.db.IGF_COLL.remove({ "_id": ObjectId(gameId) })
    return redirect(url_for("get_games"))

# add a game to the database
@app.route("/add_game", methods=["POST"])
def add_game():
    games=mongo.db.IGF_COLL
    games.insert_one(request.form.to_dict())
    return redirect(url_for('get_games'))

# random --add comment--
@app.route("/random_game")
def random_game():
    #generate a random number between 0 and the number of documents in the database
    #subtract 1 from the number of documents to prevent index bounds issues
    random_number = randint(0, (mongo.db.IGF_COLL.count() - 1))
    selected_game=mongo.db.IGF_COLL.find()[random_number]
    return render_template("dedicated.html", game=mongo.db.IGF_COLL.find_one({ '_id': ObjectId(selected_game["_id"]) }))

#for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):