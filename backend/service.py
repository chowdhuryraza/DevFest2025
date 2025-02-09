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

from deep_translator import GoogleTranslator
from twilio.twiml.voice_response import VoiceResponse, Say
from twilio.rest import Client

langcode_to_iso39 = {
  "hi-IN": "hi",
  "en-GB": "en",
  "cmn-CN": "zh",
  "yue-HK": "yue",
  "arb": "ar",
  "ta-IN": "ta",
  "vi-VN": "vi"
}


prescription_blueprint = Blueprint('prescriptions', __name__)

connection_string = f"mongodb+srv://A:{os.getenv('DB_PASSWORD')}@cluster0.xks5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

db = client["devfest"]
prescription_tb = db["prescription"]
recipient_tb = db["recipients"]

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


def make_call(recipient_id, document):
  recipient = recipient_tb.find_one({"_id": ObjectId(recipient_id)})
  if not recipient:
    print(f"Recipient with ID {recipient_id} not found")
    return

  phone_number = recipient.get('phone')
  language = recipient.get('language')
  if not phone_number or not language:
    print(f"missing info")
    return
  
  medication = document['medication']
  dosage = document['dosage']
  status = document['status']

  print(phone_number, language, medication, dosage, status)
  if status == "active":
    print("make call")
    # agregrate presecription and recipeient info and then make call

    message = f"Hello! you need to take {medication} with a dosage of {dosage} right now"
    translated_message = GoogleTranslator(source='en', target=langcode_to_iso39[language]).translate(message)
    print(translated_message)
    response = VoiceResponse()
    response.say(translated_message, language='hi-IN', loop=2)


    call = client.calls.create(
        to=phone_number,
        from_="+18885925103",  # Your Twilio phone number
        twiml=response.to_xml()
    )

    print(call.sid)

# DAYS OF WEEK NEED TO BE CAPILTALIZED
# TIMES ARE IN 24 hour format

def check_prescriptions():
  response = prescription_tb.find({})
  current_day = datetime.now().strftime('%A')
  current_time = datetime.now().strftime('%H:%M')
  current_time_dt = datetime.strptime(current_time, '%H:%M')

  for document in response:
    schedule = document.get('schedule', [])
    for entry in schedule:
      print(entry)
      if entry['day'] == current_day:
        print("YES")
        scheduled_time_dt = datetime.strptime(entry['time'], '%H:%M')
        time_difference = abs((scheduled_time_dt - current_time_dt).total_seconds() / 60)
        if time_difference <= 20:
            recipient_id = document['recipient_id']
            make_call(recipient_id, document)
            print(f"Prescription due for {document['_id']} at {current_time} on {current_day}")

check_prescriptions()