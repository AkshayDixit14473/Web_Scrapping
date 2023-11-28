import requests
#from bs4 import BeautifulSoup
from lxml import html
from http import cookies
from requests import session
urlfo = "https://www.connect2nsccl.com"
urlcm = "https://www.connect2nsccl.com/risk-cm/#/risk-management/member-cm-margin"
#cookies = dict (name ='akshay', password ='1234')
#r=requests.get(urlcm)
session = requests.Session()
print(session)

print(session.headers)
print(session.cookies)
response = session.get('https://www.connect2nsccl.com/risk-cm/#/risk-management/member-cm-margin')

print(session.headers)
print(session.cookies)
#print(r.cookies)
#htmlContent= r.content
#print(htmlContent)
# Got the html
#tree =html.fromstring(r.content)
#elements = tree.xpath('/html/body/app-root/div/risk-management/section/margin-cm-member/div/div/div/cm-member-total-margin/div/div[1]/div[1]/div/table/tbody/tr/td[9]')
#soup = BeautifulSoup(r.text,features="html5lib")
#print(soup.prettify)
#print(tree)
#print(type(elements))
#print(elements[:])
#title = soup.title
#print(title)

#paras = soup.find_all('p')
#print(paras)

#anchors = soup.find_all('p')
#print(anchors)
#print(soup.find('table'))
#print(soup.get_text())
#column_data = tables.find_all('td')
#print(column_data)
#document.querySelector("#wrapper > risk-management > section > margin-cm-member > div > div > div > cm-member-total-margin > div > div:nth-child(1) > div:nth-child(1) > div > table > tbody > tr > td:nth-child(9)")
#<td _ngcontent-ohh-42="" class="text-right">0.00%</td>

#/html/body/app-root/div/risk-management/section/margin-cm-member/div/div/div/cm-member-total-margin/div/div[1]/div[1]/div/table/tbody/tr/td[9]

custom_header = {'hello':'hello_888'}
response = session.get('https://www.connect2nsccl.com/risk-cm/#/risk-management/member-cm-margin')
