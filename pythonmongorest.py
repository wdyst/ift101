# mongorest.py
# Please use Python 3.8.6 https://www.python.org/downloads/release/python-386/
# Windows x86-64 executable installer: https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe
# macOS 64-bit installer: https://www.python.org/ftp/python/3.8.6/python-3.8.6-macosx10.9.pkg
# Linux Gzipped source tarball: https://www.python.org/ftp/python/3.8.6/Python-3.8.6.tgz
from flask import Flask
from flask_restx import Api, Resource, fields
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBName'] = 'stars'
# Change the MONGO_URI with provided connection String in Canvas
app.config['MONGO_URI'] = 'mongodb+srv://ift101:AY3qamqzeI4rHOBn@cluster0.qw7goz5.mongodb.net/restdb/?retryWrites=true&w=majority/'

@app.route('/star', methods=['GET'])
def get_all_stars():
    star = mongo.db.stars
    output = []
    for s in star.find():
        output.append({'name': s['name'], 'distance': s['distance']})
    return jsonify({'result': output})

@app.route('/star', methods=['POST'])
def add_star():
    star = mongo.db.stars
    name = request.json['name']
    distance = request.json['distance']
    star_id = star.insert({'name':name, 'distance': distance})
    new_star = star.find_one({'_id': star_id })
    output = {'name': new_star['name'], 'distance': new_star['distance']}
    return jsonify({'result' : output})

// Updated function get_connection 10/7/2022
def get_connection(self):
    try:
        client = MongoClient(MongoDbConnection.CONNECTION_STR)
        db = client.restdb
        return db
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(debug=True)
