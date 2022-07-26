from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("-profile")
options.add_argument("/home/askar/snap/firefox/common/.mozilla/firefox/tc2j6nxr.default-release")
driver = webdriver.Firefox(executable_path='/home/askar/Py/Selen/geckodriver/geckodriver', options=options)
url = 'https://web.whatsapp.com/'

try:
    driver.get(url=url)
    time.sleep(20)
    contact = "whatbot"
    input_box_search_xpath = "//div[@data-testid='chat-list-search']"
    input_box_search = WebDriverWait(driver, 30).until(
        lambda driver: driver.find_element(By.XPATH, input_box_search_xpath))
    input_box_search.click()
    time.sleep(10)
    input_box_search.send_keys(contact)
    time.sleep(10)
    selected_contact = driver.find_element(By.XPATH, "//span[@title='" + contact + "']")
    selected_contact.click()
    time.sleep(10)
    inp_xpath = "//div[@title='Введите сообщение']"
    input_box = driver.find_element(By.XPATH, inp_xpath)
    time.sleep(2)
    # input_box.send_keys("#" + Keys.ENTER)
    input_box.send_keys("#")
    btn_send_xpath = "//button[@data-testid='compose-btn-send']"
    btn_send = driver.find_element(By.XPATH, btn_send_xpath)
    btn_send.click()
    time.sleep(20)
    # driver.quit()
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
