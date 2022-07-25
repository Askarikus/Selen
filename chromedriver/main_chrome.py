from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='/home/askar/Py/Selen/chromedriver/chromedriver')
url = 'https://web.whatsapp.com/'

try:
    driver.get(url=url)
    time.sleep(60)

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()