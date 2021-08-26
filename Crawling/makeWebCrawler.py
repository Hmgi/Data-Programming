import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

driver = webdriver.Chrome('C:\\Users\hk335\Desktop\chromedriver_win32 (1)\chromedriver')

uid = 'hk335078'
upw = 'ksy331008'  # 네이버 로그인 페이지로 이동

url = ('https://nid.naver.com/nidlogin.login')

driver.get(url)
time.sleep(2)

# 아이디
tag_id = driver.find_element_by_name('id')
# 패스워드
tag_pw = driver.find_element_by_name('pw')

tag_id.click()
pyperclip.copy(uid)
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

tag_pw.click()
pyperclip.copy(upw)
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
login_btn = driver.find_element_by_id('log.login')
login_btn.click()
time.sleep(2)
