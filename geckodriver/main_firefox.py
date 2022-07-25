from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument("-profile")
options.add_argument("/home/askar/snap/firefox/common/.mozilla/firefox/tc2j6nxr.default-release")
driver = webdriver.Firefox(executable_path='/home/askar/Py/Selen/geckodriver/geckodriver', options=options)
url = 'https://web.whatsapp.com/'

try:
    driver.get(url=url)
    time.sleep(60)

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()