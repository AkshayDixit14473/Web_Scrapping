import time
from selenium import webdriver

import requests
from lxml import html

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser

# Navigate to the login page
driver.get('https://www.connect2nsccl.com')

# Wait for 5 seconds (adjust as needed)
time.sleep(100)

print("Logged in.")

# Continue with data scraping after 5 seconds
# Replace this with your logic to check if the user has logged in automatically

# urlcm = "https://www.connect2nsccl.com/risk-cm/#/risk-management/member-cm-margin"
# r=requests.get(urlcm)
# tree =html.fromstring(r.content)
# elements = tree.xpath('/html/body/app-root/div/risk-management/section/margin-cm-member/div/div/div/cm-member-total-margin/div/div[1]/div[1]/div/table/tbody/tr/td[9]')
# print(type(elements))
# print(elements[:])

# Scraping the data - replace with your actual scraping logic
# For demonstration, let's just print the page title
print("Scraped Data:")
print("Page Title:", driver.title)

# Close the browser
driver.quit()
