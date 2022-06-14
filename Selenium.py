import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://naver.com'

driver = webdriver.Chrome("/Users/admin/sources/YuGiOh-discord-bot/YuGiOh-discord-bot/chromedriver")
driver.get(url=URL)
