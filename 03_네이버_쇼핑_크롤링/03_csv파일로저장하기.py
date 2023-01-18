from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트

from webdriver_manager.chrome import ChromeDriverManager

import time

import csv

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

#  스크롤 전 높이
before_h = driver.execute_script('return window.scrollY')

# 무한 스크롤 >> 반복문
while True:
    # 맨 아래로 스크롤을 내린다
    driver.find_element('css selector','body').send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = driver.execute_script('return window.scrollY')

    if after_h == before_h:
        break
    before_h = after_h

# 파일 생성
f = open(r'C:\WebCrawling\03_네이버_쇼핑_크롤링\data.csv', 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)


# 상품정보 div
items = driver.find_elements('css selector','.basicList_info_area__TWvzp')
count = 1
for item in items:
    name = item.find_element('css selector','.basicList_title__VfX3c').text
    try:
        price = item.find_element('css selector','.price_num__S2p_v').text
    except:
        price = '판매중단'
    link = item.find_element('css selector','.basicList_title__VfX3c > a').get_attribute
    print(name, price, link)
    csvWriter.writerow([name, price, link])

# 파일 닫기
f.close() 