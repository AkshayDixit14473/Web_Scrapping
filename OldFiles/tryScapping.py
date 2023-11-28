import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser

# Navigate to the login page
login_url = 'https://ims.connect2nsccl.com/MemberPortal/'  # Replace with the login URL
driver.get(login_url)

# Wait for a few seconds for manual login (you can handle login manually)
input("Please log in manually and press Enter once logged in...")

try:
    # Modify the XPath or selector to match the element indicating a successful login
    login_indicator = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/p')
    print("User is logged in.")
except NoSuchElementException:
    print("User is not logged in.")

# Navigate to a different URL after login
target_url = 'https://example.com/another-page'  # Replace with the URL you want to visit
driver.get(target_url)

# Wait for some time to ensure the page is loaded (adjust as needed)
time.sleep(5)

# Use the provided XPath to locate the specific element
element = driver.find_element_by_xpath('/html/body/app-root/div/risk-management/section/margin-cm-member/div/div/div/cm-member-total-margin/div/div[1]/div[1]/div/table/tbody/tr/td[9]')

# Extract the data from the element
data = element.text
print("Scraped Data from the provided XPath:", data)

# Close the browser
driver.quit()
