# imports
import time
import datetime
import os

from twillioAlerts import twilioAlerts
from sendTelegramMessage import telegramAlerts

totalMarginUtilPctLimit = 80.0
alertRecipients = ['+919057243109', '+919971434484', '+919716331649']
###################### Raman ######## Ashish ######### Abhishek###
# alertRecipients = ['+919057243109']
telegramRecipients = ['1111882666', '5659720225', '6676279881']
###################### Raman ######## Ashish ###### Abhishek###
# telegramRecipients = ['1111882666']
sendAlerts = True
sleepTime = 60
cooldownTime = 10*sleepTime # should be multiple of sleepTime
telegramAlertDelay = 15*sleepTime # delay time between two telegram msgs # should be multiple of sleepTime
closingTimeH = 15
closingTimeM = 30

segment = 'FO'

######################### PASTE FROM HERE ###########################
import requests

cookies = {
    'bowfp': 'e00b00b3615c917ee30e3184f206e55b',
    'srvt': 'm1UL0OkpMbM3MHdbfQVqB5ZFALQobMOnDofKbiwBhzNx-vZBKcAGgpXSpgaZDOJv',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'bowfp=e00b00b3615c917ee30e3184f206e55b; srvt=m1UL0OkpMbM3MHdbfQVqB5ZFALQobMOnDofKbiwBhzNx-vZBKcAGgpXSpgaZDOJv',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'ufp': 'e00b00b3615c917ee30e3184f206e55b',
}

response = requests.get(
    'https://www.connect2nsccl.com/risk-fo/tm-margins-summery-level-I/JSON:JSON',
    cookies=cookies,
    headers=headers,
)
############################# TO HERE ###############################
# check if requests url matches the one in while loop

tempdate = datetime.datetime.now().date()
currdate = tempdate.strftime('%Y%m%d')
tempfilename = currdate+segment+'MARGIN.csv'

currdir = os.getcwd()
segmentdir = currdir+'/'+segment+'Margins'

if not os.path.exists(segmentdir):
    print("Directory "+segment+"Margins does exists, creating ", segmentdir)
    os.makedirs(segmentdir)


filename = os.path.join(segmentdir, tempfilename)

print("Writing at: ", filename)

if not os.path.isfile(filename):
    with open(filename, 'a') as file:
        file.write("Time,TotalMargin,TotalMarginUtil\n")

myAlerts = twilioAlerts()
myTelegramAlerts = telegramAlerts()
cooldownWait = 0
telegramTimer = 0
while datetime.datetime.now().time() < datetime.time(closingTimeH,closingTimeM):
    response = requests.get(
    'https://www.connect2nsccl.com/risk-fo/tm-margins-summery-level-I/JSON:JSON',
    cookies=cookies,
    headers=headers,
    )


    try:
        data = response.json()
    except:
        print("Error: Cannot fetch data, please update cookies.")
        exit(0)
    
    totalMargin = data["data"]["result"][0]['totalMargin']
    totalMarginUtilPct = data["data"]["result"][0]['tmMrgnUtilisation']
    # timestamp = data['data']['timestamp'][-8:]
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')

    if telegramTimer == 0:
        for recipient in telegramRecipients:
            formatted_pct = "{:.2f}".format(totalMarginUtilPct)
            telegramMsg = segment+ " margin: "+str(formatted_pct)+"%."
            myTelegramAlerts.sendTelegramMsgAlert(recipient, telegramMsg)
        telegramTimer = telegramAlertDelay
    
    if sendAlerts:
        if totalMarginUtilPct >= totalMarginUtilPctLimit:
            formatted_pct = "{:.2f}".format(totalMarginUtilPct)
            alertMsg = segment + " margin has reached "+str(formatted_pct)+"%."
            if cooldownWait==0:
                for recipient in alertRecipients:
                    myAlerts.sendMsgAlert(recipient, alertMsg)
                    myAlerts.sendCallAlert(recipient, alertMsg)
                cooldownWait = cooldownTime
                for recipient in telegramRecipients:
                    myTelegramAlerts.sendTelegramMsgAlert(recipient, alertMsg)
            print(timestamp, alertMsg)
    
    currData = str(timestamp)+","+str(totalMargin)+","+str(totalMarginUtilPct)
    print(currData)

    with open(filename, 'a') as file:
        file.write(currData+"\n")
    
    if cooldownWait>0:
        cooldownWait-=sleepTime
    telegramTimer -= sleepTime

    time.sleep(sleepTime)



