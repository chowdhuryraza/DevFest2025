import os
from twilio.rest import Client 
from twilio.twiml.voice_response import VoiceResponse, Say

from dotenv import load_dotenv
load_dotenv()

from flask import Blueprint, request, jsonify
from bson import ObjectId
import os
from flask import session, jsonify
import pymongo
from pymongo import MongoClient
import requests
import certifi
from datetime import datetime

prescription_blueprint = Blueprint('prescriptions', __name__)

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

db = client["devfest"]
prescription_tb = db["prescription"]
recipient_tb = db["recipients"]

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def make_call(recipient_id, language):
  recipient = recipient_tb.find_one({"_id": ObjectId(recipient_id)})
  if not recipient:
    print(f"Recipient with ID {recipient_id} not found")
    return

  phone_number = recipient.get('phone')
  if not phone_number:
    print(f"Phone number for recipient {recipient_id} not found")
    return

  # agregrate presecription and recipeient info and then make call

  # call = twilio_client.calls.create(
  #     to=phone_number,
  #     from_="+1234567890",  # Your Twilio phone number
  #     url=call_url
  # )

  # print(call.sid)


# DAYS OF WEEK NEED TO BE CAPILTALIZED
# TIMES ARE IN 24 hour format

def check_prescriptions():
  response = prescription_tb.find({})
  current_day = datetime.now().strftime('%A')
  current_time = datetime.now().strftime('%H:%M')
  print(response, current_day, current_time)
  for document in response:
    schedule = document.get('schedule', [])
    for entry in schedule:
      print(entry)
      if entry['day'] == current_day and entry['time'] == current_time:
        recipient_id = document['recipient_id']
        make_call(recipient_id, document)
        print(f"Prescription due for {document['_id']} at {current_time} on {current_day}")

check_prescriptions()