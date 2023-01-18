from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트

from webdriver_manager.chrome import ChromeDriverManager

import time

# 브라우저 꺼짐 방지

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)



# 불필요한 에러 메시지 없애기

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])



service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)


# browser = webdriver.Chrome("C:\chromedriver.exe")
# 웹페이지 해당 주소 이동

driver.get("https://www.naver.com")
driver.implicitly_wait(10) # 로딩될때까지 10초 대기

# 쇼핑 메뉴 클릭
driver.find_element('css selector','a.nav.shop').click()
# 딜레이 명령어
time.sleep(2)

# 쇼핑 메뉴안 검색창 클릭 
search = driver.find_element('css selector','input._searchInput_search_text_fSuJ6')
search.click()

# 검색어 입력
search.send_keys('아이폰 14')
search.send_keys(Keys.ENTER)