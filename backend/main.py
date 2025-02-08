import pymongo
import os
from pymongo import MongoClient
import requests
import certifi
from dotenv import load_dotenv
load_dotenv()

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

db = client["devfest"]
guardiantb = db["guardian"]

""" create/insert one post to db guardian collection """
# post = { "_id": 4, "name": "poopooo", "email": "hahaha@gmail.com" }
# guardiantb.insert_one(post)
# insert_many(lists_of_posts)

""" read/find posts by specifying attributes to search by, can be multiple """
response = guardiantb.find({ "_id": 2 })
# returns cursor object, loop through iterable cursor to access dictionaries of each document that meets query
# find_one() useful for id specific queries
for result in response:
  print(result)

res = guardiantb.find_one({ "_id": 0})
print(res)

# no paramter queries will return all collection documents

""" delete one or many posts by specifiyng matching parameters """
guardiantb.delete_one({ "_id": 0 })
guardiantb.delete_many( { "email": "ss7373@columbia.edu" })

""" update one or many with search query and update operator fields """
# $rename, $set, $unset
# rename renames the field
# set changes the field value
guardiantb.update_one({ "name": "chow" }, { "$set": { "name": "raza chow" } })

""" can count # of documents for specific query """
total_documents = guardiantb.count_documents({  })
print(total_documents)

### TESTING ONLY; DELETE LATER
print()
print("hello")
print(guardiantb.count_documents({}))
for x in guardiantb.find():
  print(x)

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def hello_world():
  print("hi")
  return "<p>Hello, World!</p>"

@app.route("/", methods=["POST"])
def hello_world_post():
  print("POST gang")
  print(request.json.get("hi"))
  guardiantb.insert_one(request.json)
  print("Number of documents in guardiantb: " + str(guardiantb.count_documents({})))
  for x in guardiantb.find():
    print(x)
  print()
  return "<p>Hello, World!</p>"