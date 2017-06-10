import requests
from bs4 import BeautifulSoup
import re
import webbrowser

regex = re.compile(r"https://scontent*?\s")



r = open("https://www.instagram.com/p/BUqORd2BwRN5o5lyKSchC8II8waiW6ZL7dwKpM0/")

soup = BeautifulSoup(r.read())
print(r.text)

print(soup.find_all('class="_icyx7"'))

