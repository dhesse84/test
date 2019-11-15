#import os

#from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo
#import scrape_mars

#from flask import restful
#from flask import make_response
#from bson.json_util import dumps

############
import pymongo
import json
from bson.json_util import dumps
from flask import Flask, render_template, Markup, request, redirect
import requests
#from flask_static_compress import FlaskStaticCompress
#import logging


# Create an instance of Flask
app = Flask(__name__)


mongo = pymongo.MongoClient('mongodb+srv://danh:pJmVMOcSjYNZ87rt@cluster0-zhzxw.mongodb.net/test?retryWrites=true', maxPoolSize=50, connect=False)

db = pymongo.database.Database(mongo, 'test')
col = pymongo.collection.Collection(db, 'sample_mflix')

mars = {'text':'hi there'}

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def home():
    """Landing page."""
    #mars = db.col.find_one()    
    col_results = json.loads(dumps(col.find().limit(5)))
    mars = list(col_results)

    return render_template("index.html", mars=mars)

###########

########################
#MONGO_URL = os.environ.get('MONGO_URL')
#if not MONGO_URL:
#    MONGO_URL = "mongodb://localhost:27017/rest"


#app.config['MONGO_URI'] = 'mongodb+srv://danh:pJmVMOcSjYNZ87rt@cluster0-zhzxw.mongodb.net/test?retryWrites=true'

#client = pymongo.MongoClient('mongodb+srv://danh:pJmVMOcSjYNZ87rt@cluster0-zhzxw.mongodb.net/test?retryWrites=true')

# Use PyMongo to establish Mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
#mongo = PyMongo(app)
#db = mongo[sample_mflix]
############################




# Route to render index.html template using data from Mongo



# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    #mars_data = scrape_mars.scrape_info()  #codefile.def_name()

    #Drops collection if available to remove duplicates
    #mongo.db.collection.drop()
    
    mars_data = "hello world"
    mars = {'text':'well hello to you, too'}
    #mongo.sample_mflix.comments.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
