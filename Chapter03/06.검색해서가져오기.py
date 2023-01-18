import requests
from bs4 import BeautifulSoup
import pyautogui
keyword = pyautogui.prompt('검색어를 입력하세요>>>')
response = requests.get(f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={keyword}')
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit')

for link in links:   
    title = link.text
    url = link.attrs['href'] 
    print(title, url)