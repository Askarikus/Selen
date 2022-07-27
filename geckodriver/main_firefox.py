from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class MyDriver():
    def __init__(self):
        self.options = Options()
        self.options.add_argument("-profile")
        self.options.add_argument("/home/askar/snap/firefox/common/.mozilla/firefox/tc2j6nxr.default-release")
        # self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(executable_path='/home/askar/Py/Selen/geckodriver/geckodriver',
                                        options=self.options)

    #
    # def get_url(self, url, time_wait):
    #     self.driver.get(url=url)
    #     time.sleep(time_wait)
    #
    # def webdriverwaituntil(self, time_wait, xpath_string):
    #     return WebDriverWait(self.driver, 30).until(
    #         lambda driver: driver.find_element(By.XPATH, xpath_string))
    #
    # def click_on_element(self, time_wait, element):
    #     element.click()
    #     time.sleep(time_wait)
    #
    # def send_keys_to_element(self, keys, time_wait, element):
    #     element.send_keys(keys)
    #     time.sleep(time_wait)
    #
    # def find_element_by_xpath(self, xpath_string):
    #     return self.driver.find_element(By.XPATH, xpath_string)

    def open_whatsapp_message_window(self, contact):
        self.driver.get(url='https://web.whatsapp.com/')
        time.sleep(30)
        # ждем пока не подгрузятся элементы ввода
        input_box_search_xpath = "//div[@data-testid='chat-list-search']"
        input_box_search = WebDriverWait(self.driver, 30).until(
            lambda driver: driver.find_element(By.XPATH, input_box_search_xpath))
        # отправляем в поле ввода наименование контакт(бота)
        input_box_search.click()
        time.sleep(10)
        input_box_search.send_keys(contact)
        time.sleep(10)
        # кликаем на поле контакт
        selected_contact = self.driver.find_element(By.XPATH, "//span[@title='" + contact + "']")
        selected_contact.click()
        time.sleep(10)

    def get_whatsapp_last_messages(self, n):
        messages_xpath = "//div[@class='_2wUmf message-in focusable-list-item']"
        last_messages = self.driver.find_elements(By.XPATH, messages_xpath)[-1]
        return last_messages.text[:n]



