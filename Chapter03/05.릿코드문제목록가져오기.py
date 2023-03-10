from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import time
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

driver.get('https://leetcode.com/tag/Shell/')
# driver.implicitly_wait(10)
time.sleep(10)
html = driver.page_source
# driver.quit()

soup = BeautifulSoup(html, 'html.parser')
problems = soup.select('.title-cell__ZGos > a')

for problem in problems:
    url = problem.attrs['href']
    title = problem.text
    print(url, title)

# print(problems)    

