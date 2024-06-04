# server.py -- This file is adapted from my bachelor thesis (https://github.com/phuef/ba)

from flask import Flask, jsonify, request, json, send_file
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)
#import logging
#logging.basicConfig(filename='error.log',level=logging.DEBUG)

# returns the filtered json data
def get_data(string):
    f= "ToDO: get the data from mongodb"
    data = json.load(f)
    if string:
        help=[]
        for i in data: # adjust according to the data in mongodb
            if string in i["topics"] or re.search(rf"{string}", i["url"]):#or re.search(rf"{string}", i["microlink"]["data"]["description"])
                help.append(i)
        return help
    return data

@app.route('/search', methods=['GET'])
def get_tasks():
    '''
    returns results for a search
    '''
    if request.method == 'GET':
        args = request.args
        search_query=args.get("search_query") # =birds, wenn /search?search_query=birds 
        return jsonify(get_data(search_query))

@app.route('/img', methods=['GET'])
def get_img():
    '''
    Returns preview images for websites
    '''
    if request.method == 'GET':
        args = request.args
        img=args.get("img") 
        return send_file("data/previewImages/" +img)
    
if __name__ == '__main__':
    app.run(debug=True)