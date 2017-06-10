#! python3
import re
import webbrowser
import requests
from bs4 import BeautifulSoup
import sys

regex = re.compile(r'(https?:\/\/.*?\.(?:png|jpg))')

link = ''.join(sys.argv[1:])


r = requests.get(link)

new=2

meh =re.findall(regex,r.text)
url = meh[0]

webbrowser.open(url,new=new)