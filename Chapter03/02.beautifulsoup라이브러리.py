import requests
from bs4 import BeautifulSoup

response = requests.get('https://leetcode.com/tag/quickselect/')
html = response.text
soup = BeautifulSoup(html, 'html.parser')
content = soup.select_one('#app > .ant-row content__xk8m')
print(content)