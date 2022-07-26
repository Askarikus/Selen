from datetime import time
from unittest import TestCase

from geckodriver.main_firefox import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


def main_menu_send_sharp():
    url = 'https://web.whatsapp.com/'
    try:
        # открываем страницу
        driver.get(url=url)
        time.sleep(30)
        contact = "whatbot"
        text = "#"
        # ждем пока не подгрузятся элементы ввода
        input_box_search_xpath = "//div[@data-testid='chat-list-search']"
        input_box_search = WebDriverWait(driver, 30).until(
            lambda driver: driver.find_element(By.XPATH, input_box_search_xpath))
        # отправляем в поле ввода наименование контакт(бота)
        input_box_search.click()
        time.sleep(10)
        input_box_search.send_keys(contact)
        time.sleep(10)
        # кликаем на поле контакт
        selected_contact = driver.find_element(By.XPATH, "//span[@title='" + contact + "']")
        selected_contact.click()
        time.sleep(10)
        # находим элемент поле ввода сообщения
        inp_xpath = "//div[@title='Введите сообщение']"
        input_box = driver.find_element(By.XPATH, inp_xpath)
        time.sleep(2)
        # input_box.send_keys("#" + Keys.ENTER)
        # вводим заранее сохраненный текст
        input_box.send_keys(text)
        btn_send_xpath = "//button[@data-testid='compose-btn-send']"
        # жмём отправить
        btn_send = driver.find_element(By.XPATH, btn_send_xpath)
        btn_send.click()
        time.sleep(20)
        messages_xpath = "//div[@class='_2wUmf message-in focusable-list-item']"
        last_messages = driver.find_elements(By.XPATH, messages_xpath)[-1]
        return last_messages.text[:38]
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()


class ManFunctionsTestCase(TestCase):
    def test_main_menu_send_sharp(self):
        result = main_menu_send_sharp()
        self.assertEqual(' Привет.\n\nНа связи бот сервиса Wahelp,', result)
