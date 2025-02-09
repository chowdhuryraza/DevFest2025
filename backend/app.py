import os
import pymongo
import requests
import certifi

from dotenv import load_dotenv
from flask import Flask 
from pymongo import MongoClient
from flask import request, jsonify, session
from flask_session import Session
from bson import ObjectId
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from routes.guardians import guardian_blueprint
from routes.recipients import recipient_blueprint
from routes.prescriptions import prescription_blueprint
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your_super_secret_key'
Session(app)

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

# connect with mongodb and set collection variables
db = client["devfest"]
call_log_tb = db["call_log"]
guardian_tb = db["guardian"]

# register blueprint routes
app.register_blueprint(guardian_blueprint, url_prefix='/guardians')
app.register_blueprint(recipient_blueprint, url_prefix='/recipients')
app.register_blueprint(prescription_blueprint, url_prefix='/prescriptions')

# LOGIN
@app.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  email = data['email']
  password = data['password']

  person = guardian_tb.find_one({ "email": email })
  if not person:
    return jsonify({'message': 'user does not exist'}), 400

  if check_password_hash(person['password_hash'], password):
    session['user'] = {'email': person['email'], 'id': str(person['_id'])}  # add user info to current session
    return jsonify({'message': 'login success'}), 200
  
  return jsonify({'message': 'incorrect password'}), 400

# REGISTER
@app.route('/register', methods=['POST'])
def register():
  name = request.json.get("name")
  email = request.json.get("email")
  password = request.json.get("password")
  phone = request.json.get("phone")

  existing_guardian = guardian_tb.find_one({"email": email})
  if existing_guardian:
    return jsonify({'message': 'user already exists'}), 400

  hashed_password = generate_password_hash(password)
  print(password)
  print(hashed_password)
  
  document = {
      "name": name,
      "email": email,
      "password_hash": hashed_password,
      "phone": phone
  }
  
  res = guardian_tb.insert_one(document)
  if not res.acknowledged:
    return jsonify({'message': 'Unable to create user'}), 404
  
  return jsonify({'message': 'user created'}), 201

# LOGOUT
@app.route('/logout', methods=['POST'])
def logout():
  session.pop('user', None)
  return jsonify({'message': 'logout successful'}), 201


@app.route('/get_call_logs', methods=['GET'])
def get_call_logs():
  call_logs = list(call_log_tb.find({ }))
  return jsonify(call_logs), 200

if __name__ == "__main__":
  app.run(debug=True)