from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from bson import ObjectId
import os
from flask import session, jsonify

import pymongo
from pymongo import MongoClient
import requests
import certifi

prescription_blueprint = Blueprint('prescriptions', __name__)

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

# connect with mongodb and set collection variables
db = client["devfest"]
prescription_tb = db["prescription"]
recipient_tb = db["recipients"]

@prescription_blueprint.route('/create', methods=['POST'])
def create_prescription():
  # if 'user' not in session:
  #   return jsonify({'message': 'please log in'}), 404
  # document = request.get_json() # frontend ensures all fields exist
  # print(document["recipient_id"])

  # recipient = recipient_tb.find_one({ "_id": ObjectId(document["recipient_id"]) })
  
  # if not recipient:
  #   return jsonify({'message': 'Recipient not found'}), 404
  
  # document["recipient_id"] = recipient["_id"]
  # document["recipient_id"] = recipient["_id"]
  
  # res = prescription_tb.insert_one(document)
  # recipient_tb.update_one({ "_id": recipient["_id"] }, { "$push": { "prescriptions": res.inserted_id } })
  
  # if not res.acknowledged:
  #   return jsonify({'message': 'Error Creating Perscription'}), 404
  
  # return jsonify({'message': 'Prescription has been created'}), 200

  medication = request.json.get("medication")
  dosage = request.json.get("dosage")
  instructions = request.json.get("instructions")
  day = request.json.get("day")
  time = request.json.get("time")
  status = request.json.get("status")
  print(medication, dosage, day, time, status)
  document = {
      "medication": medication,
      "dosage": dosage,
      "instructions": instructions,
      "schedule": [{"day": day, "time": time}],
      "status": status
  }
  print(document)

  res = prescription_tb.insert_one(document)
  if not res.acknowledged:
    return jsonify({'message': 'Unable to create prescription'}), 404
  
  return jsonify({'message': 'prescription created'}), 201

@prescription_blueprint.route('/update/<prescription_id>', methods=['POST'])
def update_prescription(prescription_id):
  if 'user' not in session:
    return jsonify({'message': 'please log in'}), 404
  updated_document = request.get_json()
  res = prescription_tb.update_one({ "_id": ObjectId(prescription_id) }, { "$set": updated_document })
  
  if not res.acknowledged:
    return jsonify({'message': 'update invalid'}), 404
  
  return jsonify({'message': 'Prescription has been updated'}), 200

@prescription_blueprint.route('/<prescription_id>', methods=['GET'])
def get_prescription(prescription_id):
  if 'user' not in session:
    return jsonify({'message': 'please log in'}), 404
  prescription = prescription_tb.find_one({ "_id": ObjectId(prescription_id) })
  if not prescription:
    return jsonify({'message': 'Prescription not found'}), 404
  
  return jsonify(prescription), 200

@prescription_blueprint.route('/all', methods=['GET'])
def get_all_prescriptions():
  # if 'user' not in session:
  #   return jsonify({'message': 'please log in'}), 404
  prescriptions = list(prescription_tb.find({ }))
  for i in range(len(prescriptions)):
    prescriptions[i]['_id'] = str(prescriptions[i]['_id'])

    if 'recipient_id' in prescriptions[i]:
      prescriptions[i]['recipient_id'] = str(prescriptions[i]['recipient_id'])

  return jsonify(prescriptions), 200