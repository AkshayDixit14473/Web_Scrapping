from bs4 import BeautifulSoup

import requests

cookies = {
    'ak_bmsc': '6B858F16F57C615990F673C0E783FD71~000000000000000000000000000000~YAAQZF06Fx5BFx2LAQAAoNs5IxX/qQx4HFvxAt1HtgFCW5/hPhWFfzyl+qR7eZopu2IinSTeWZ526ysVl+0jLpoIjQSS70Rt7EWS3Ym0CkK8fRA54u1y5UYbcTfC3g+o2GCGFvCrn7CqxA5lYzJ6Dbu3yduCnfOe+Rs1IftNUqMh+AgHvH5BWRube6wrgDQX0zH+gX+w6prrPIrk7j5XNYRrJXNgyhD3BO0UNlcAekP+QfEfUNOv891WWANKYETixv7R7Ev0HrNTpKFTIjpHEPfwNEBGRY9b5bwULJ6fHZFc8pVN5S0js56lcO/cdJ1PnivMt7Pz3Cm0tPW1BxtR2c3ABPBlzv84wXoDy6iigNPlg+zLDqkFODsGc0CA/p3/XzzD3zZg6R3sl62kbCK91qsy71dJyHPFTMaK1cCWCRW16lO+gdnHCc+AAv5BySUtb/esm34pJ2ov+0Z719/M3QatmNVTLQnOKd84WhlcdDNBAHY4jvaesA3597Y=',
    'bm_sv': '2BFED597308A577D625A778361C265AE~YAAQZF06F/60Fx2LAQAALG5KIxWcVwXUEWeOk7Wp0+jsPoJlMXM74yYtuBvh1wqdkhRL0kRVEAH9+spZ63eeLvLkkZHozKxu5V83gEWu8e2bzgpbRa6AjPtRFFbo6QgMEEZmlaErVL6NzZZpnRNp9R0xwaXRx+f7RbhQpdFf9rgpm+MGiSZVQUfwFjdsJej5VnG3PtuJW+BlLQhKsTMUJvjOoXcavkTpCE+vwwQiREYzgsbLnVPE6063RyP+Ank9jgk2YlUJFa0=~1',
    'bowfp': 'e0b7b3f664dda6eb81a55e14c0e626d8',
    'srvt': 'hmGOkLV-uZ8rcFag9zbvNf6k06swLFy1PuiSkgF1AArhjqgil1tU_mH8nT4uR-0G',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'ak_bmsc=6B858F16F57C615990F673C0E783FD71~000000000000000000000000000000~YAAQZF06Fx5BFx2LAQAAoNs5IxX/qQx4HFvxAt1HtgFCW5/hPhWFfzyl+qR7eZopu2IinSTeWZ526ysVl+0jLpoIjQSS70Rt7EWS3Ym0CkK8fRA54u1y5UYbcTfC3g+o2GCGFvCrn7CqxA5lYzJ6Dbu3yduCnfOe+Rs1IftNUqMh+AgHvH5BWRube6wrgDQX0zH+gX+w6prrPIrk7j5XNYRrJXNgyhD3BO0UNlcAekP+QfEfUNOv891WWANKYETixv7R7Ev0HrNTpKFTIjpHEPfwNEBGRY9b5bwULJ6fHZFc8pVN5S0js56lcO/cdJ1PnivMt7Pz3Cm0tPW1BxtR2c3ABPBlzv84wXoDy6iigNPlg+zLDqkFODsGc0CA/p3/XzzD3zZg6R3sl62kbCK91qsy71dJyHPFTMaK1cCWCRW16lO+gdnHCc+AAv5BySUtb/esm34pJ2ov+0Z719/M3QatmNVTLQnOKd84WhlcdDNBAHY4jvaesA3597Y=; bm_sv=2BFED597308A577D625A778361C265AE~YAAQZF06F/60Fx2LAQAALG5KIxWcVwXUEWeOk7Wp0+jsPoJlMXM74yYtuBvh1wqdkhRL0kRVEAH9+spZ63eeLvLkkZHozKxu5V83gEWu8e2bzgpbRa6AjPtRFFbo6QgMEEZmlaErVL6NzZZpnRNp9R0xwaXRx+f7RbhQpdFf9rgpm+MGiSZVQUfwFjdsJej5VnG3PtuJW+BlLQhKsTMUJvjOoXcavkTpCE+vwwQiREYzgsbLnVPE6063RyP+Ank9jgk2YlUJFa0=~1; bowfp=e0b7b3f664dda6eb81a55e14c0e626d8; srvt=hmGOkLV-uZ8rcFag9zbvNf6k06swLFy1PuiSkgF1AArhjqgil1tU_mH8nT4uR-0G',
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

response = requests.get('https://www.connect2nsccl.com/risk-cm/cm-total-margins/JSON:JSON', cookies=cookies, headers=headers)
data = response.json()
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
# print(type(soup))
# print(data)
# print(type(data))
for k in data["data"]["result"]:
    if(k=="totalMrgnUtil"):
        print(k,": ", data["data"]["result"][k])
    if(k=="utilPct"):
        print(k,": ", data["data"]["result"][k])


