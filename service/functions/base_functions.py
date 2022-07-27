from service.requests_to.yclients import add_one_record
from service.requests_to.yclients import add_day_to_master
import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from geckodriver.main_firefox import MyDriver


def main_menu_send_sharp():
    mydriver = MyDriver()
    try:
        contact = "whatbot"
        text = "#"
        mydriver.open_whatsapp_message_window(contact=contact)
        # находим элемент поле ввода сообщения
        inp_xpath = "//div[@title='Введите сообщение']"
        input_box = mydriver.driver.find_element(By.XPATH, inp_xpath)
        # вводим заранее сохраненный текст
        input_box.send_keys(text)
        # жмём отправить
        btn_send_xpath = "//button[@data-testid='compose-btn-send']"
        btn_send = mydriver.driver.find_element(By.XPATH, btn_send_xpath)
        btn_send.click()
        time.sleep(20)
        return mydriver.get_whatsapp_last_messages(38)
    except Exception as e:
        print(e)
    finally:
        mydriver.driver.close()
        mydriver.driver.quit()


def create_item_yclients():
    company_id = 210108
    customer_askar_id_9196070897 = 151643371
    master_customer_nikita_id = 1986247
    master_nikita_tester_id = 3846611
    date_now_str = datetime.datetime.now().strftime('%Y-%m-%d')
    url_yclients = 'https://yclients.com/timetable/{}#main_date={}&mode=1'.format(company_id, date_now_str)
    mydriver = MyDriver()
    try:
        # открываем страницу
        mydriver.driver.get(url=url_yclients)
        time.sleep(30)
        dict_cookies = {i['name']: i['value'] for i in mydriver.driver.get_cookies()}
        # add_day_to_master(dict_cookies, company_id, master_customer_nikita_id, "2022-07-24")
        add_one_record(dict_cookies, company_id, master_nikita_tester_id, customer_askar_id_9196070897)
        # canvas_xpath = '//canvas[@data-engagement-hint-target-id="engagement-hint-manager-timetable-canvas"]'
        contact = "whatbot"
        mydriver.open_whatsapp_message_window(contact=contact)
        return mydriver.get_whatsapp_last_messages(38)
    except Exception as e:
        print(e)
    finally:
        mydriver.driver.close()
        mydriver.driver.quit()
