from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("-profile")
options.add_argument("/home/askar/snap/firefox/common/.mozilla/firefox/tc2j6nxr.default-release")
driver = webdriver.Firefox(executable_path='/home/askar/Py/Selen/geckodriver/geckodriver', options=options)
