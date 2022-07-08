import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action'

input = 'SPYRAL-지니어스'

driver = webdriver.Chrome("./chromedriver")
driver.get(url=URL)

time.sleep(1)
search_box = driver.find_element_by_id('keyword')
search_box.send_keys(input)
search_box.send_keys(Keys.RETURN)
time.sleep(1)

print(driver.find_element_by_id('card_image_0_1').get_attribute("src"))
print(driver.find_element_by_id('card_image_0_1').get_attribute('alt'))
# test = driver.find_elements_by_class_name("box_card_text c_text flex_1")

