import os
from twilio.rest import Client 
from twilio.twiml.voice_response import VoiceResponse, Say

response = VoiceResponse()
response.say('हेलो भाई तुम पागल हो और भारी दवाई हो', language='hi-IN', loop=2)

account_sid = "AC166961d3413aa5f3055e40669d830f3c"
auth_token = "0152c98041f84b8d14740afe8d65e9b6"
client = Client(account_sid, auth_token)

call = client.calls.create(
  # url="http://demo.twilio.com/docs/voice.xml",
  twiml=response.to_xml(),
  to="+13472809173",
  from_="+18885925103",
)

print(call.sid)