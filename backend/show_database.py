import pymongo
import os
from pymongo import MongoClient
import requests
import certifi
from dotenv import load_dotenv
load_dotenv()

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

db = client["devfest"]
guardiantb = db["guardian"]

for x in guardiantb.find():
    print(x)
    print()