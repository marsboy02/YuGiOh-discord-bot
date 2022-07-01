import selenium
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

search_box = driver.find_element_by_id('keyword')
search_box.send_keys(input)
search_box.send_keys(Keys.RETURN)

# js에서 코드 긁어와야 함
# 가져와야하는것 카드이름, 카드사진, 카드설명, 공격력,수비력
title = driver.find_element_by_xpath('//span[@id="card_image_0_1"]').text
print(title)

