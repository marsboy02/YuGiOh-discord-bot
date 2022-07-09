import selenium
import time
from selenium import webdriver
import os
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

URL = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action'

def search(input):
    driver = webdriver.Chrome("CHROMEDRIVER_PATH")
    driver.get(url=URL)

    search_box = driver.find_element_by_id('keyword')
    search_box.send_keys(input)
    search_box.send_keys(Keys.RETURN)

    time.sleep(1)
    string = ''
    # (driver.find_element_by_id('card_image_0_1').get_attribute("src")) 카드 이미지 링크

    string += '카드명:' + driver.find_element_by_id('card_image_0_1').get_attribute('alt') + '\n'
    string += '설명:' + driver.find_element_by_class_name("card_info_species_and_other_item").text + '\n'
    string += '속성:' + driver.find_element_by_class_name("box_card_attribute").text + '\n'
    string += '공격력:' + driver.find_element_by_class_name("atk_power").text + '\n'
    string += '수비력:' + driver.find_element_by_class_name("def_power").text + '\n'
    string += '효과:' + driver.find_element_by_xpath("//dl[@class='flex_1']/dd[@class='box_card_text c_text flex_1']").text

    return string
