import re
import webbrowser
import requests
from bs4 import BeautifulSoup

regex = re.compile(r'(https?:\/\/.*?\.(?:png|jpg))')

link = input()

print(re.findall(regex,link))

r = requests.get(link)

new=2

meh =re.findall(regex,r.text)
print(meh)
url = meh[0]

webbrowser.open(url,new=new)