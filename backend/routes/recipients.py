from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from bson import ObjectId
import os

import pymongo
from pymongo import MongoClient
import requests
import certifi

recipient_blueprint = Blueprint('recipients', __name__)

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

# connect with mongodb and set collection variables
db = client["devfest"]
recipient_tb = db["recipients"]


@recipient_blueprint.route('/create_recipient', methods=['POST'])
def create_recipient():
  document = request.get_json() # frontend ensures all fields exist
  res = recipient_tb.insert_one(document)
  if not res.acknowledged:
    return jsonify({'message': 'unable to create'}), 404
  
  return jsonify({'message': 'Recipient has been created'}), 200

@recipient_blueprint.route('/update_recipient/<recipient_id>', methods=['POST'])
def update_recipient(recipient_id):
  updated_document = request.get_json()
  res = recipient_tb.update_one({ "_id": ObjectId(recipient_id) }, { "$set": updated_document })
  if not res.acknowledged:
    return jsonify({'message': 'update invalid'}), 404
  
  return jsonify({'message': 'Recipient has been updated'}), 200

@recipient_blueprint.route('/get_recipient/<recipient_id>', methods=['GET'])
def get_recipient(recipient_id):
  recipient = recipient_tb.find_one({ "_id": ObjectId(recipient_id) })
  if not recipient:
    return jsonify({'message': 'Recipient not found'}), 404
  
  return jsonify(recipient), 200

@recipient_blueprint.route('/get_recipients', methods=['GET'])
def get_recipients():
  recipients = list(recipient_tb.find())
  return jsonify(recipients), 200