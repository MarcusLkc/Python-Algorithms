import requests
from bs4 import BeautifulSoup
import re

regex = re.compile(r"https://scontent*?\s")


r = requests.get("https://www.instagram.com/p/BUqORd2BwRN5o5lyKSchC8II8waiW6ZL7dwKpM0/")

soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify)

print(soup.find_all('meta'))

