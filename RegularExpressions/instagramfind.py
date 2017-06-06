import requests
from bs4 import BeautifulSoup
import re

regex = re.compile(r"https://scontent*?\s")


r = requests.get("https://www.instagram.com/p/BT4QXTvjiZl/")

soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify)

print(soup.find_all('meta'))

