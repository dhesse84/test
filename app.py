import os

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

from flask.ext import restful
from flask import make_response
from bson.json_util import dumps


########################
MONGO_URL = os.environ.get('MONGO_URL')
#if not MONGO_URL:
#    MONGO_URL = "mongodb://localhost:27017/rest";

# Create an instance of Flask
app = Flask(__name__)

app.config['MONGO_URI'] = MONGO_URL

# Use PyMongo to establish Mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
mongo = PyMongo(app)
############################



# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars = mongo.db.collection.find_one()
    # Return template and data
    return render_template("index.html", mars=mars)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    #mars_data = scrape_mars.scrape_info()  #codefile.def_name()

    #Drops collection if available to remove duplicates
    #mongo.db.collection.drop()
    
    mars_data = "hello world"
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
