from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from bson import ObjectId
import os

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


@guardian_blueprint.route('/get_guardians', methods=['GET'])
def get_all_guardians():
  all_guardians = guardian_tb.find({ })
  res = []

  for guardian in all_guardians:
    guardian["_id"] = str(guardian["_id"]) # convert BSON object into string for serialization
    res.append(guardian)
    print(guardian["_id"])
  
  return jsonify(res), 200

@guardian_blueprint.route('/guardians/<guardian_id>', methods=['GET'])
def get_one_guardian(guardian_id):
  person = guardian_tb.find_one({ "_id": ObjectId(guardian_id) })
  if not person:
    return jsonify({'message': 'Guardian not found'}), 404

  person["_id"] = str(person["_id"]) 
  return jsonify(person), 200

@guardian_blueprint.route('/delete_guardian/<guardian_id>', methods=['GET'])
def delete_guardian(guardian_id):
  res = guardian_tb.delete_one({ "_id": ObjectId(guardian_id) })
  if not res.acknowledged:
    return jsonify({'message': 'Guardian not found'}), 404
  
  return jsonify({'message': 'Guardian has been deleted'}), 200

# FIX THIS
@guardian_blueprint.route('/create_guardian', methods=['POST'])
def create_guardian():
  name = request.json.get("name")
  email = request.json.get("email")
  password = request.json.get("password")
  phone = request.json.get("phone")

  existing_guardian = guardian_tb.find_one({"email": email})
  if existing_guardian:
    return jsonify({'message': 'Guardian already exists'}), 400
  
  document = {
      "name": name,
      "email": email,
      "password": generate_password_hash(password),
      "phone": phone
    }
  
  res = guardian_tb.insert_one(document)
  if not res.acknowledged:
    return jsonify({'message': 'Unable to create guardian'}), 404
  
  # Guardian.create_user(guardian_tb, email, generate_password_hash(password), name, phone)
  return jsonify({'message': 'Guardian created successfully'}), 201
  
@guardian_blueprint.route('/update_guardian/<guardian_id>', methods=['POST'])
def update_guardian(guardian_id):
  updated_document = request.get_json()
  res = guardian_tb.update_one({ "_id": ObjectId(guardian_id) }, { "$set": updated_document })
  if not res.acknowledged:
    return jsonify({'message': 'update invalid'}), 404
  
  return jsonify({'message': 'Guardian has been updated'}), 200