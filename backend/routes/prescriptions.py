from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from bson import ObjectId
from models import Guardian
import os

import pymongo
from pymongo import MongoClient
import requests
import certifi

prescription_blueprint = Blueprint('prescriptions', __name__)

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

# connect with mongodb and set collection variables
db = client["devfest"]
prescription_tb = db["prescriptions"]

@prescription_blueprint.route('/create_prescription', methods=['POST'])
def create_prescription():
  document = request.get_json() # frontend ensures all fields exist
  res = prescription_tb.insert_one(document)
  if not res.acknowledged:
    return jsonify({'message': 'unable to create'}), 404
  
  return jsonify({'message': 'Prescription has been created'}), 200

@prescription_blueprint.route('/update_prescription/<prescription_id>', methods=['POST'])
def update_prescription(prescription_id):
  updated_document = request.get_json()
  res = prescription_tb.update_one({ "_id": ObjectId(prescription_id) }, { "$set": updated_document })
  if not res.acknowledged:
    return jsonify({'message': 'update invalid'}), 404
  
  return jsonify({'message': 'Prescription has been updated'}), 200

@prescription_blueprint.route('/get_prescription/<prescription_id>', methods=['GET'])
def get_prescription(prescription_id):
  prescription = prescription_tb.find_one({ "_id": ObjectId(prescription_id) })
  if not prescription:
    return jsonify({'message': 'Prescription not found'}), 404
  
  return jsonify(prescription), 200

@prescription_blueprint.route('/get_prescriptions', methods=['GET'])
def get_prescriptions():
  prescriptions = list(prescription_tb.find({ }))
  return jsonify(prescriptions), 200

