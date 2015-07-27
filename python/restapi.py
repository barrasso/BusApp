import json
import bottle
import pymongo
from bottle import route, run, request, abort
from bottle import request, response, get, post
from bottle import static_file, redirect, HTTPResponse
from bottle import mako_view as view
from pymongo import MongoClient
from bson.json_util import dumps
 
connectionString = 'mongodb://admin:busapp123@7a51ab267b24f5353eafcab51fbb5bdc/dfw-c9-0.objectrocket.com:37190,dfw-c9-1.objectrocket.com:37190/busapp?w=1'

## init Mongo client
client = MongoClient()

## connect to MongoDB
client = MongoClient(connectionString)
print('Connecting to client: %s') % client

## get Bus App databse
db = client['busapp']
print('Connected to database: %s') % db

## get collections
busCollection = db['buses']
studentCollection = db['students']
     
@route('/getStudents')
def get_students():
    results = studentCollection.find()
    print results

    # return bottle.template('result', {"results":results})
    # studentCollection = 
    # return studentCollection
 
run(host='localhost', port=8080)