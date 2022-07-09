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

# input = 'SPYRAL-지니어스'

# driver = webdriver.Chrome("./chromedriver")
# driver.get(url=URL)
#
# time.sleep(1)
# search_box = driver.find_element_by_id('keyword')
# search_box.send_keys(input)
# search_box.send_keys(Keys.RETURN)
# time.sleep(2)
#
# print(driver.find_element_by_id('card_image_0_1').get_attribute("src"))
# print(driver.find_element_by_id('card_image_0_1').get_attribute('alt'))
# print(driver.find_element_by_class_name("card_info_species_and_other_item").text)
# print(driver.find_element_by_class_name("box_card_attribute").text)
# print(driver.find_element_by_class_name("atk_power").text)
# print(driver.find_element_by_class_name("def_power").text)
# time.sleep(3)
# print(driver.find_element_by_xpath("//dl[@class='flex_1']/dd[@class='box_card_text c_text flex_1']").text)

def search(input):
    driver = webdriver.Chrome("./chromedriver")
    driver.get(url=URL)

    time.sleep(1)
    search_box = driver.find_element_by_id('keyword')
    search_box.send_keys(input)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    print(driver.find_element_by_id('card_image_0_1').get_attribute("src"))
    print(driver.find_element_by_id('card_image_0_1').get_attribute('alt'))
    print(driver.find_element_by_class_name("card_info_species_and_other_item").text)
    print(driver.find_element_by_class_name("box_card_attribute").text)
    print(driver.find_element_by_class_name("atk_power").text)
    print(driver.find_element_by_class_name("def_power").text)
    time.sleep(3)
    print(driver.find_element_by_xpath("//dl[@class='flex_1']/dd[@class='box_card_text c_text flex_1']").text)
