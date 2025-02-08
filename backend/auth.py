from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.security import generate_password_hash

import os, certifi
from dotenv import load_dotenv
load_dotenv()

from models import User

app = Flask(__name__)
CORS(app)

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

db = client["devfest"]
guardian_tb = db["guardian"]
recepient_tb = db["recepient"]
prescription_tb = db["prescription"]
call_log_tb = db["call_log"]


@app.route("/home")
def index():
    return "<p>Hello, World!</p>"

@app.route("/register", methods = ["POST"])
def register():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    phone = request.json.get("phone")

    try:
        found_user = User(guardian_tb, email)
        found_user.set_password(password)
    except ValueError:
        User.create_user(guardian_tb, email, generate_password_hash(password), name, phone)


if __name__ == '__main__':
    app.run(debug=True)
