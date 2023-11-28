import requests

class telegramAlerts:
  def __init__(self) -> None:
    self.TelegramBotCredential = '6495422079:AAGApwK7v0_QGJ-0E621jD1YyTTYHeckBSU'
    self.randKey = "$9avZYt!B!"

  def sendTelegramMsgAlert(self, recipient, msg = "This is a alert"):
    try:
        Url = "https://api.telegram.org/bot" + str(self.TelegramBotCredential) + "/sendMessage?chat_id="+ str(recipient)
        textdata ={ "text" :msg}
        response = requests. request ( "POST",Url, params=textdata)
    except Exception as e:
        Message = str(e) + ": Exception occur in SendMessageToTelegram"
        print (Message)
