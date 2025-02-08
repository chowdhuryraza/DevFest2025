import os
from twilio.rest import Client 
from twilio.twiml.voice_response import VoiceResponse, Say

from dotenv import load_dotenv
load_dotenv()

response = VoiceResponse()
response.say('हेलो भाई तुम पागल हो और भारी दवाई हो', language='hi-IN', loop=2)

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

call = client.calls.create(
  # url="http://demo.twilio.com/docs/voice.xml",
  twiml=response.to_xml(),
  to="+13472809173",
  from_="+18885925103",
)

print(call.sid)