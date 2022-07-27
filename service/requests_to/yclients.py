import requests


def add_day_to_master(dict_cookies, company_id, master_customer_id, day_format):
    headers = {
        "Connection": "keep-alive",
        "Host": "yclients.com",
        "Referer": "https://yclients.com/timetable/{}".format(company_id),
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Site": "same-origin",


        "Accept": "text/html, */*; q=0.01",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",

        "X-Yclients-Application-Platform": "legacy JS-1.0",
        "X-Yclients-Application-Version": "1.0.0",
        "X-Yclients-Application-Name": "biz.erp.web",
        "X-Yclients-Application-Action": "journal_record_masters",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Content-Length": "117"
    }
    body_data = {
        "master_id": master_customer_id,
        "intervals[0][from]": 32400,
        "intervals[0][to]": 86400,
        "days[]": day_format,
        "reload_id": 7029
    }
    # cookies = {
    #     "__cf_bm": "g3ngQ2_nmuip4fxSpgnm99rewQtGFDU6y4kowXHHWrI-1658859074-0-ARKz3XQxtsbZJbp3KuMZ0b5citlausXwFwrE1kkrRqmWe9I3UE7VkqkfI6Do8acvOnu2iCdMmKkdY9fT2A47A7o=",
    #     "_cfuvid": "AXYjeS6cM1CCZxcWVkTHJ7Isfjc5yCq0Zv47qB7ll2g-1658859074391-0-604800000",
    #     "_auth": "u-5047526-87456f3be9bf4cd6ae1ff4",
    #     "_ycl_language_id": "1"
    # }
    url_req = "https://yclients.com/timetable/addDaysToMaster/"
    req = requests.post(url=url_req, data=body_data, headers=headers, cookies=dict_cookies)


def add_one_record(dict_cookies, company_id, master_id, customer_id):
    headers = {
        "Connection": "keep-alive",
        "Host": "yclients.com",
        "Referer": "https://yclients.com/timetable/{}".format(company_id),
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Site": "same-origin",

        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",

        "X-Yclients-Application-Platform": "legacy JS-1.0",
        "X-Yclients-Application-Version": "1.0.0",
        "X-Yclients-Application-Name": "biz.erp.web",
        "X-Yclients-Application-Action": "record",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Content-Length": "1787"
    }
    body_data = {
        "id": 0,
        "salon_id": company_id,
        "services[0][id]": master_id,
        "services[0][amount]": 1,
        "services[1][id]": 8412190,
        "services[1][amount]": 1,
        "services_info[3846611][id]": master_id,
        "services_info[3846611][length]": 3600,
        "services_info[3846611][price_max]": 0.00,
        "services_info[3846611][price_min]": 0.00,
        "services_info[3846611][title]": "Консультация по внедрению Wahelp для YCLIENTS",
        "services_info[8412190][id]": 8412190,
        "services_info[8412190][length]": 3600,
        "services_info[8412190][price_max]": 0.00,
        "services_info[8412190][price_min]": 0.00,
        "services_info[8412190][title]": "Консультация по интеграции Wahelp с Bitrix24",
        "resource_instances[]": 0,
        "master_id": 1986247,
        "date": 1658088000,
        "time": 32400,
        "end_time": 39600,
        "ts": 1658130300,
        "length": 7200,
        "comment": "comment_1",
        "phone": "919 607-08-97",
        "phone_country_id": 1,
        "name": "Аскар",
        "email": "askarikus@list.ru",
        "comer_title": "",
        "client_discount": 0,
        "client_deleted": "false",
        "fb": "",
        "max_length": 32400,
        "max_ts": 43200,
        "add_client": 0,
        "send_sms_now": 1,
        "sms_hour": 0,
        "email_hour": 0,
        "save_sure": 0,
        "visit_id": 0,
        "visit": 0,
        "active": 1,
        "master_request": 1,
        "new_service_id": 8412190,
        "record_from": "",
        "from_url": "",
        "from_url_short": "",
        "is_mobile": 0,
        "attendance": 0,
        "custom_color": "e91e63",
        "has_payments": 0,
        "fast_payment": 0,
        "activity_id": 0,
        "print_bill": 0,
        "fast_payment_bank": 0,
        "is_sale_bill_printed": "false",
        "notified": 0,
        "payment_status": 0,
        "client_id": customer_id,
        "comer_id": "",
        "recordDeleteAccess": 0,
        "hasSalonRecordsFormClientAccess": 1,
        "recordEditFullPaidAccess": 1,
        "real_length": 7200,
        "clients_count": 1,
        "reload_id": 7029
    }
    url_req = "https://yclients.com/admin_record/save/"
    req = requests.post(url=url_req, data=body_data, headers=headers, cookies=dict_cookies)
