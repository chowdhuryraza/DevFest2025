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
from flask_cors import CORS

from werkzeug.security import generate_password_hash
from models import Guardian

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


@app.route('/get_guardians', methods=['GET'])
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

@app.route('/delete_guardian/<guardian_id>', methods=['GET'])
def delete_guardian(guardian_id):
  res = guardian_tb.delete_one({ "_id": ObjectId(guardian_id) })
  if not res.acknowledged:
    return jsonify({'message': 'Guardian not found'}), 404
  
  return jsonify({'message': 'Guardian has been deleted'}), 200

@app.route('/create_guardian', methods=['POST'])
def create_guardian():
  # document = request.get_json() # frontend ensures all fields exist
  # res = guardian_tb.insert_one(document)
  # if not res.acknowledged:
  #   return jsonify({'message': 'unable to create'}), 404
  
  # return jsonify({'message': 'Guardian has been created'}), 200
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
  
  Guardian.create_user(guardian_tb, email, generate_password_hash(password), name, phone)
  return jsonify({'message': 'Guardian created successfully'}), 201
  

@app.route('/update_guardian/<guardian_id>', methods=['POST'])
def update_guardian(guardian_id):
  updated_document = request.get_json()
  res = guardian_tb.update_one({ "_id": ObjectId(guardian_id) }, { "$set": updated_document })
  if not res.acknowledged:
    return jsonify({'message': 'update invalid'}), 404
  
  return jsonify({'message': 'Guardian has been updated'}), 200

@app.route('/create_recipient', methods=['POST'])
def create_recipient():
  document = request.get_json() # frontend ensures all fields exist
  res = recepient_tb.insert_one(document)
  if not res.acknowledged:
    return jsonify({'message': 'unable to create'}), 404
  
  return jsonify({'message': 'Recipient has been created'}), 200

@app.route('/update_recipient/<recipient_id>', methods=['POST'])
def update_recipient(recipient_id):
  updated_document = request.get_json()
  res = recepient_tb.update_one({ "_id": ObjectId(recipient_id) }, { "$set": updated_document })
  if not res.acknowledged:
    return jsonify({'message': 'update invalid'}), 404
  
  return jsonify({'message': 'Recipient has been updated'}), 200

@app.route('/get_recipient/<recipient_id>', methods=['GET'])
def get_recipient(recipient_id):
  recipient = recepient_tb.find_one({ "_id": ObjectId(recipient_id) })
  if not recipient:
    return jsonify({'message': 'Recipient not found'}), 404
  
  return jsonify(recipient), 200

@app.route('/get_recipients', methods=['GET'])
def get_recipients():
  recipients = list(recepient_tb.find())
  return jsonify(recipients), 200

@app.route('/create_prescription', methods=['POST'])
def create_prescription():
  document = request.get_json() # frontend ensures all fields exist
  res = prescription_tb.insert_one(document)
  if not res.acknowledged:
    return jsonify({'message': 'unable to create'}), 404
  
  return jsonify({'message': 'Prescription has been created'}), 200

@app.route('/update_prescription/<prescription_id>', methods=['POST'])
def update_prescription(prescription_id):
  updated_document = request.get_json()
  res = prescription_tb.update_one({ "_id": ObjectId(prescription_id) }, { "$set": updated_document })
  if not res.acknowledged:
    return jsonify({'message': 'update invalid'}), 404
  
  return jsonify({'message': 'Prescription has been updated'}), 200

@app.route('/get_prescription/<prescription_id>', methods=['GET'])
def get_prescription(prescription_id):
  prescription = prescription_tb.find_one({ "_id": ObjectId(prescription_id) })
  if not prescription:
    return jsonify({'message': 'Prescription not found'}), 404
  
  return jsonify(prescription), 200

@app.route('/get_prescriptions', methods=['GET'])
def get_prescriptions():
  prescriptions = list(prescription_tb.find({ }))
  return jsonify(prescriptions), 200

@app.route('/get_call_logs', methods=['GET'])
def get_call_logs():
  call_logs = list(call_log_tb.find({ }))
  return jsonify(call_logs), 200


if __name__ == "__main__":
  app.run(debug=True)