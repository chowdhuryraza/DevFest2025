"""
TO DOS

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

from routes.guardians import guardian_blueprint
from routes.recipients import recipient_blueprint
from routes.prescriptions import prescription_blueprint

load_dotenv()

app = Flask(__name__)

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

# connect with mongodb and set collection variables
db = client["devfest"]
call_log_tb = db["call_log"]

app.register_blueprint(guardian_blueprint, url_prefix='/guardians')
app.register_blueprint(recipient_blueprint, url_prefix='/recipients')
app.register_blueprint(prescription_blueprint, url_prefix='/prescriptions')

@app.route('/get_call_logs', methods=['GET'])
def get_call_logs():
  call_logs = list(call_log_tb.find({ }))
  return jsonify(call_logs), 200

if __name__ == "__main__":
  app.run(debug=True)