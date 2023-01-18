from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
# 크롬 드라이버 자동 업데이트

from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐 방지

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)



# 불필요한 에러 메시지 없애기

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])



service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)


# browser = webdriver.Chrome("C:\chromedriver.exe")
# 웹페이지 해당 주소 이동
driver.implicitly_wait(5) # 로딩될때까지 10초 대기
driver.maximize_window() # 화면 최대화
driver.get("https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsearch.shopping.naver.com%2Fsearch%2Fall%3Fquery%3D%25EC%2595%2584%25EC%259D%25B4%25ED%258F%25B0%252014%26cat_id%3D%26frm%3DNVSHATC")

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, '#id')
id.click()
pyperclip.copy('thehrto12')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
# 비번 입력창
pw = driver.find_element(By.CSS_SELECTOR, '#pw')
pw.click()
pyperclip.copy('tpgjs9494')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
# 로그인 버튼 
login = driver.find_element(By.CSS_SELECTOR, '#log\.login')
login.click()

driver.implicitly_wait(5) # 로딩될때까지 5초 대기

# 해외로그인 차단 인증창
phone = driver.find_element(By.CSS_SELECTOR, '#phone_value')
phone.click()
phone.send_keys('01062818739')

# 확인버튼
ok = driver.find_element(By.CSS_SELECTOR, '#oab\.submit')
ok.click()
