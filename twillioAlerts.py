# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

from twilio.twiml.voice_response import Say

class twilioAlerts:
  def __init__(self) -> None:
    self.account_sid = "id"
    self.auth_token = "token"
    self.number = 'number'
    self.randKey = "key"
    self.twilio_client = Client(self.account_sid, self.auth_token)

  def sendMsgAlert(self, recipient, msg = "This is a alert"):
    message = self.twilio_client.messages.create(
      from_=self.number,
      body=msg + " "+self.randKey,
      to=recipient)
    
  def sendCallAlert(self, recipient, msg = "This is a alert"):
    call = self.twilio_client.calls.create(
      twiml='<Response><Say>'+msg+'</Say></Response>',
      to=recipient,
      from_=self.number)




# myAlert = Alerts()
# myAlert.sendCallAlert("no1", "The margin is above 80%.")
# myAlert.sendMsgAlert("no1", "The margin is above 80%.")
