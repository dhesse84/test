############
import os
import pymongo
import json
from bson.json_util import dumps
from flask import Flask, render_template, Markup, request, redirect
import requests
############
import zipfile
import pathlib
from pathlib import Path
############
from collections import defaultdict
import re
import string
############

# Create an instance of Flask
app = Flask(__name__)

#MONGO_URL = os.environ.get('MONGO_URL')
MONGO_URL = "mongodb+srv://danh:pJmVMOcSjYNZ87rt@cluster0-zhzxw.mongodb.net/test?retryWrites=true&w=majority"

myclient = pymongo.MongoClient(MONGO_URL, maxPoolSize=50, connect=True)
#mongo = pymongo.MongoClient('mongodb+srv://danh:pJmVMOcSjYNZ87rt@cluster0-zhzxw.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)

mars = {'text':'BLANK','count':0}
search_term = "Jaime Lannister"


@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def home():
    """Landing page."""
    return render_template("index.html", stuff=mars)


@app.route("/send")
def send():

    mars_data = "BLANK"
    mars['text'] = 'BLANK'

    mydb = myclient["sample_mflix"]
    mycol = mydb["comments"]
    myquery = {'name': search_term }
    mydoc = json.loads(dumps(mycol.find(myquery)))
    myclient.close()
    
    mars['email'] = mydoc[0]['email']
    mars['count'] += 1

    # Redirect back to home page
    #return render_template("index.html", mars=mars)
    return redirect("/")


@app.route("/injest")
def injest():
    unzip_path = 'static/data/unzip/'

### unzip files
    pathlib.Path(unzip_path).mkdir(parents=False, exist_ok=True)
    with zipfile.ZipFile('static/data/data.zip', 'r') as zip_ref:
        zip_ref.extractall(unzip_path)
###

### word counts
    main_dict = {}
    all_filepaths = []
    for (root,dirs,files) in os.walk(unzip_path, topdown=True):
        if files != []:
            dirname = str(root.split("\\")[-1])
            main_dict[dirname] = {}
        
            for (file) in files:
                filename = str(Path(file).with_suffix(''))
                main_dict[dirname][filename] = {}
            
                frequency_dict = defaultdict(int)
                docpath = open(f'{root}\{file}', 'r', encoding='utf8')
                fulltext = docpath.read()
            
                try:
                    doctitle = re.search("<title=(.*)>", fulltext).group(1)
                except:
                    doctitle = ''
                try:
                    docdate = re.search("<date=(.*)>", fulltext).group(1)
                except:
                    docdate = ''
                main_dict[dirname][filename]['title'] = doctitle
                main_dict[dirname][filename]['date'] = docdate
            
                lowtext = fulltext.lower()
                words_list = str.split(lowtext)
                for word in words_list:
                    frequency_dict[word] += 1

                main_dict[dirname][filename]['word_count'] = frequency_dict
                main_data = json.dumps(main_dict)
###

### write db
    mydb = myclient["example_db"]
    mycol = mydb["example_coll"]
    
    #drop database
    mycol.drop()

    #with open('static/data/somedata.json') as J:
    #    file_data = json.load(J)
    #print(file_data)

    mycol.insert_one(main_data)
    myclient.close()
###

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
