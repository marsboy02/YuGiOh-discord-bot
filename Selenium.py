from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome('chromedrive의 경로를 입력')

driver.get('URL')

time.sleep(3)

'''
크롬드라이버 설치
https://www.db.yugioh-card.com/yugiohdb/card_search.action URL
키워드 입력 후 엔터 -> 검색 완료
'''