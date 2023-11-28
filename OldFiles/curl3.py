from bs4 import BeautifulSoup

import requests

cookies = {
    'bowfp': 'e0b7b3f664dda6eb81a55e14c0e626d8',
    'srvt': 'nnNujFu8tXISnKQZy4Gu21wasavmD2siV5mGUrfzNfLS8WO1FlUKVFcecg03jHke',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'bowfp=e0b7b3f664dda6eb81a55e14c0e626d8; srvt=nnNujFu8tXISnKQZy4Gu21wasavmD2siV5mGUrfzNfLS8WO1FlUKVFcecg03jHke',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'ufp': 'e0b7b3f664dda6eb81a55e14c0e626d8',
}

response = requests.get(
    'https://www.connect2nsccl.com/risk-cm/member-total-margins/JSON:JSON',
    cookies=cookies,
    headers=headers,
)

data = response.json()
# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
# print(type(soup))
# print(data)
# print(type(data))
print(data['data']['result'][0])
# print(type(data['data']['result'][0]))
for k in data['data']['result'][0]:
    if(k=='totalMrgn'):
        print(k,": ", data["data"]["result"][0][k])
    if(k=="tmMrgnUtilPct"):
        print(k,": ", data["data"]["result"][0][k])
print('totalMrgn',": ", data["data"]["result"][0]['totalMrgn'])
print('tmMrgnUtilPct',": ", data["data"]["result"][0]['tmMrgnUtilPct'])
print(data['data']['timestamp'][-8:])
