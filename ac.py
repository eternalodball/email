#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep
import random

#webdriver

url = "https://www.instagram.com/accounts/emailsignup/"
CHROME_DVR_DIR = "webdrivers/chromedriver"
browser = webdriver.Chrome(executable_path=CHROME_DVR_DIR)

#ClearCache before opening url (currently not working)

#browser.get('chrome://settings/clearBrowserData')
#browser.find_element_by_id('clearBrowsingDataConfirm').click()

#Open ig signup url
browser.get(url)

#elements

time.sleep(4)
email = browser.find_element_by_css_selector('div.WZdjL:nth-child(4) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
fullname = browser.find_element_by_css_selector('div.WZdjL:nth-child(5) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
username = browser.find_element_by_css_selector('div.WZdjL:nth-child(6) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
Password = browser.find_element_by_css_selector('div.WZdjL:nth-child(7) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
signup_button = browser.find_element_by_css_selector('div.bkEs3:nth-child(1)')

#Fields to use

my_email = 'xavob80172@balaket.com'
my_fullname = 'Aiss walker'
my_username = 'randomtor89745'
my_password = 'Password123@'

#Fill the page

email.send_keys(my_email)
fullname.send_keys(my_fullname)
username.send_keys(my_username)
Password.send_keys(my_password)
time.sleep(2)
Password.send_keys(Keys.ENTER)

#elements next page

time.sleep(3)
birthday_month = browser.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(1) > select > option:nth-child(9)')
birthday_day = browser.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(2) > select > option:nth-child(25)')
birthday_year = browser.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select > option:nth-child(26)')
birthday_next_button = browser.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.lC6p0.g6RW6 > button')

#Fill the page

birthday_month.click()
birthday_day.click()
birthday_year.click()
time.sleep(2)
birthday_next_button.click()

#otp