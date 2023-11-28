# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

from twilio.twiml.voice_response import Say

class twilioAlerts:
  def __init__(self) -> None:
    self.account_sid = "AC3f02358943d45ff1a128a1081b9bc168"
    self.auth_token = "81fbc8daf9575683fc0783830a575f8d"
    self.number = '+12565008146'
    self.randKey = "$9avZYt!B!"
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
# myAlert.sendCallAlert("+919057243109", "The margin is above 80%.")
# myAlert.sendMsgAlert("+919057243109", "The margin is above 80%.")