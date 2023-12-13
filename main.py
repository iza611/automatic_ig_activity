from time import sleep
from selenium import webdriver

browser = webdriver.Edge()

browser.get('https://www.instagram.com/')

sleep(5)

browser.close()