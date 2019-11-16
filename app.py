############
import os
import pymongo
import json
from bson.json_util import dumps
from flask import Flask, render_template, Markup, request, redirect
import requests
############

# Create an instance of Flask
app = Flask(__name__)

MONGO_URL = os.environ.get('MONGO_URL')
#if not MONGO_URL:
#    MONGO_URL = "mongodb://localhost:27017/rest"

mongo = pymongo.MongoClient(MONGO_URL, maxPoolSize=50, connect=True)
#mongo = pymongo.MongoClient('mongodb+srv://danh:pJmVMOcSjYNZ87rt@cluster0-zhzxw.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)

mars = {'text':'hi there'}

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def home():
    """Landing page."""
    #mars = json.loads(dumps(mongo.sample_mflix.comments.find_one()))
    query = {"name":"Joshua Kent"}
    mars = json.loads(dumps(mongo.sample_mflix.comments.find(query)))
    return render_template("index.html", mars=mars)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars_data = "hello world"
    mars = {'text':'well hello to you, too'}

    # Redirect back to home page
    return render_template("index.html", mars=mars)

if __name__ == "__main__":
    app.run(debug=True)
