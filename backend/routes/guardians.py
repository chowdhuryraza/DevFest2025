from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from bson import ObjectId
import os
from flask import session, jsonify

import pymongo
from pymongo import MongoClient
import requests
import certifi

guardian_blueprint = Blueprint('guardians', __name__)

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

# connect with mongodb and set collection variables
db = client["devfest"]
guardian_tb = db["guardian"]


@guardian_blueprint.route('/all', methods=['GET'])
def get_all_guardians():
  all_guardians = guardian_tb.find({ })
  res = []

  for guardian in all_guardians:
    guardian["_id"] = str(guardian["_id"]) # convert BSON object into string for serialization
    res.append(guardian)
    print(guardian["_id"])
  
  return jsonify(res), 200

@guardian_blueprint.route('/<guardian_id>', methods=['GET'])
def get_one_guardian(guardian_id):
  person = guardian_tb.find_one({ "_id": ObjectId(guardian_id) })
  if not person:
    return jsonify({'message': 'Guardian not found'}), 404

  person["_id"] = str(person["_id"]) 
  return jsonify(person), 200

@guardian_blueprint.route('/delete/<guardian_id>', methods=['GET'])
def delete_guardian(guardian_id):
  res = guardian_tb.delete_one({ "_id": ObjectId(guardian_id) })
  if not res.acknowledged:
    return jsonify({'message': 'Guardian not found'}), 404
  
  return jsonify({'message': 'Guardian has been deleted'}), 200
  
@guardian_blueprint.route('/update/<guardian_id>', methods=['POST'])
def update_guardian(guardian_id):
  updated_document = request.get_json()
  res = guardian_tb.update_one({ "_id": ObjectId(guardian_id) }, { "$set": updated_document })
  if not res.acknowledged:
    return jsonify({'message': 'update invalid'}), 404
  
  return jsonify({'message': 'Guardian has been updated'}), 200