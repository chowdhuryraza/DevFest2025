from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from bson import ObjectId
import os
from flask import session, jsonify

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
guardian_tb = db["guardian"]


@recipient_blueprint.route('/create', methods=['POST'])
def create_recipient():
  if 'user' not in session:
    return jsonify({'message': 'please log in'}), 404
  document = request.get_json() # frontend ensures all fields exist
  res = recipient_tb.insert_one(document)
  
  if not res.acknowledged:
    return jsonify({'message': 'unable to create'}), 404

  # add to guardian list of recepients
  guardian_tb.update_one(
    { "_id": ObjectId(session['user']['id']) },
    { "$push": { "recipients": res.inserted_id }}
  )

  return jsonify({'message': 'Recipient has been created'}), 200


@recipient_blueprint.route('/update/<recipient_id>', methods=['POST'])
def update_recipient(recipient_id):
    if 'user' not in session:
        return jsonify({'message': 'please log in'}), 404
    
    guardian_id = session['user']['id']
    guardian = guardian_tb.find_one({"_id": ObjectId(guardian_id)})
    
    if not guardian:
        return jsonify({'message': 'Guardian not found'}), 404
    
    recipient_ids = guardian.get('recipients', [])
    if ObjectId(recipient_id) not in recipient_ids:
        return jsonify({'message': 'Recipient not associated with this guardian'}), 403
    
    updated_document = request.get_json()
    res = recipient_tb.update_one({"_id": ObjectId(recipient_id)}, {"$set": updated_document})
    if not res.acknowledged:
        return jsonify({'message': 'update invalid'}), 404
    
    return jsonify({'message': 'Recipient has been updated'}), 200


@recipient_blueprint.route('/<recipient_id>', methods=['GET'])
def get_recipient(recipient_id):
    if 'user' not in session:
        return jsonify({'message': 'please log in'}), 404
    
    guardian_id = session['user']['id']
    guardian = guardian_tb.find_one({"_id": ObjectId(guardian_id)})
    
    if not guardian:
        return jsonify({'message': 'Guardian not found'}), 404
    
    recipient_ids = guardian.get('recipients', [])
    if ObjectId(recipient_id) not in recipient_ids:
        return jsonify({'message': 'Recipient not associated with this guardian'}), 403
    
    recipient = recipient_tb.find_one({"_id": ObjectId(recipient_id)})
    if not recipient:
        return jsonify({'message': 'Recipient not found'}), 404
    
    return jsonify(recipient), 200


@recipient_blueprint.route('/all', methods=['GET'])
def get_all_recipients():
    if 'user' not in session:
        return jsonify({'message': 'please log in'}), 404
    
    guardian_id = session['user']['id']
    guardian = guardian_tb.find_one({"_id": ObjectId(guardian_id)})
    
    if not guardian:
        return jsonify({'message': 'user not found'}), 404
    
    recipient_ids = guardian.get('recipients', [])
    recipients = list(recipient_tb.find({"_id": {"$in": recipient_ids}}))
    
    return jsonify(recipients), 200