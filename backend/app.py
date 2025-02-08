"""
TO DOS

NICE TO HAVES
  - use blueprints to seperate and organize related routes
"""

from dotenv import load_dotenv
from flask import Flask 
import os
import pymongo
from pymongo import MongoClient
import requests
import certifi
from flask import request, jsonify
from bson import ObjectId

load_dotenv()

app = Flask(__name__)

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

# connect with mongodb and set collection variables
db = client["devfest"]
guardian_tb = db["guardian"]
recepient_tb = db["recepient"]
prescription_tb = db["prescription"]
call_log_tb = db["call_log"]

""" routes for guardians """

@app.route('/guardians', methods=['GET'])
def get_all_guardians():
  all_guardians = guardian_tb.find({ })
  res = []

  for guardian in all_guardians:
    guardian["_id"] = str(guardian["_id"]) # convert BSON object into string for serialization
    res.append(guardian)
    print(guardian["_id"])
  
  return jsonify(res), 200


@app.route('/guardians/<guardian_id>', methods=['GET'])
def get_one_guardian(guardian_id):
  person = guardian_tb.find_one({ "_id": ObjectId(guardian_id) })
  if not person:
    return jsonify({'message': 'Guardian not found'}), 404

  person["_id"] = str(person["_id"]) 
  return jsonify(person), 200


@app.route('/guardians/delete/<guardian_id>', methods=['GET'])
def delete_guardian(guardian_id):
  res = guardian_tb.delete_one({ "_id": ObjectId(guardian_id) })
  if not res.acknowledged:
    return jsonify({'message': 'Guardian not found'}), 404
  
  return jsonify({'message': 'Guardian has been deleted'}), 200


@app.route('/create_guardian', methods=['POST'])
def create_guardian():
  document = request.get_json() # frontend ensures all fields exist
  print("--", document)
  res = guardian_tb.insert_one(document)
  if not res.acknowledged:
    return jsonify({'message': 'unable to create'}), 404
  
  return jsonify({'message': 'Guardian has been created'}), 200


if __name__ == "__main__":
  app.run(debug=True)