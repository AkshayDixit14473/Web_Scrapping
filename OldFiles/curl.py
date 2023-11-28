import requests
from bs4 import BeautifulSoup

cookies = {
    'JSESSIONID': '3E918B508F0C422A6A8DE506F9EA8B09',
    'bowfp': '9d4693ae9d9f8f299830d937e63c338e',
    'srvt': 'hl5mTYJf5L_01b2u7VMZQM8YkTIdEeu1LbvPgf_aKgifyLEF4NCoXHBTunH4pprY',
    'ak_bmsc': '6B858F16F57C615990F673C0E783FD71~000000000000000000000000000000~YAAQZF06Fx5BFx2LAQAAoNs5IxX/qQx4HFvxAt1HtgFCW5/hPhWFfzyl+qR7eZopu2IinSTeWZ526ysVl+0jLpoIjQSS70Rt7EWS3Ym0CkK8fRA54u1y5UYbcTfC3g+o2GCGFvCrn7CqxA5lYzJ6Dbu3yduCnfOe+Rs1IftNUqMh+AgHvH5BWRube6wrgDQX0zH+gX+w6prrPIrk7j5XNYRrJXNgyhD3BO0UNlcAekP+QfEfUNOv891WWANKYETixv7R7Ev0HrNTpKFTIjpHEPfwNEBGRY9b5bwULJ6fHZFc8pVN5S0js56lcO/cdJ1PnivMt7Pz3Cm0tPW1BxtR2c3ABPBlzv84wXoDy6iigNPlg+zLDqkFODsGc0CA/p3/XzzD3zZg6R3sl62kbCK91qsy71dJyHPFTMaK1cCWCRW16lO+gdnHCc+AAv5BySUtb/esm34pJ2ov+0Z719/M3QatmNVTLQnOKd84WhlcdDNBAHY4jvaesA3597Y=',
    'ssoticketcookie': '3E918B508F0C422A6A8DE506F9EA8B09',
    'bm_sv': '2BFED597308A577D625A778361C265AE~YAAQrF06FxlgzBqLAQAA6aNIIxWO6kTb939DkSXFhB8D4pR1omqdeszuE0Dls3Nfr8lSMV3R9dfNu0M0UDyNcK2MtB94NkI79Ht5CSejMO8RDPMoONLmSIxlYoK3Ap4DMT1bybTU9ViICJytJX973CugZSN1Gbj5Z5itIvQhtc5UnF4gyXOGF5Pxryv+hnw+hHmDiQelzIpGWj6mnpNoEk3Sui7T28KMWv7Vs7h3CZvNcY8ZY1v38MBfcW9JPqd5sxkP4mP8pWQ=~1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=3E918B508F0C422A6A8DE506F9EA8B09; bowfp=9d4693ae9d9f8f299830d937e63c338e; srvt=hl5mTYJf5L_01b2u7VMZQM8YkTIdEeu1LbvPgf_aKgifyLEF4NCoXHBTunH4pprY; ak_bmsc=6B858F16F57C615990F673C0E783FD71~000000000000000000000000000000~YAAQZF06Fx5BFx2LAQAAoNs5IxX/qQx4HFvxAt1HtgFCW5/hPhWFfzyl+qR7eZopu2IinSTeWZ526ysVl+0jLpoIjQSS70Rt7EWS3Ym0CkK8fRA54u1y5UYbcTfC3g+o2GCGFvCrn7CqxA5lYzJ6Dbu3yduCnfOe+Rs1IftNUqMh+AgHvH5BWRube6wrgDQX0zH+gX+w6prrPIrk7j5XNYRrJXNgyhD3BO0UNlcAekP+QfEfUNOv891WWANKYETixv7R7Ev0HrNTpKFTIjpHEPfwNEBGRY9b5bwULJ6fHZFc8pVN5S0js56lcO/cdJ1PnivMt7Pz3Cm0tPW1BxtR2c3ABPBlzv84wXoDy6iigNPlg+zLDqkFODsGc0CA/p3/XzzD3zZg6R3sl62kbCK91qsy71dJyHPFTMaK1cCWCRW16lO+gdnHCc+AAv5BySUtb/esm34pJ2ov+0Z719/M3QatmNVTLQnOKd84WhlcdDNBAHY4jvaesA3597Y=; ssoticketcookie=3E918B508F0C422A6A8DE506F9EA8B09; bm_sv=2BFED597308A577D625A778361C265AE~YAAQrF06FxlgzBqLAQAA6aNIIxWO6kTb939DkSXFhB8D4pR1omqdeszuE0Dls3Nfr8lSMV3R9dfNu0M0UDyNcK2MtB94NkI79Ht5CSejMO8RDPMoONLmSIxlYoK3Ap4DMT1bybTU9ViICJytJX973CugZSN1Gbj5Z5itIvQhtc5UnF4gyXOGF5Pxryv+hnw+hHmDiQelzIpGWj6mnpNoEk3Sui7T28KMWv7Vs7h3CZvNcY8ZY1v38MBfcW9JPqd5sxkP4mP8pWQ=~1',
    'Referer': 'https://ims.connect2nsccl.com/MemberPortal/validateOtp',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://ims.connect2nsccl.com/MemberPortal/updateProfile', cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
print("Here")
for data_element in data_elements:
    print(data_element.text)