import re
import requests
from bs4 import BeautifulSoup

regex = re.compile(r'"(https://scontent.*?)"')

link = "https://scontent-lga3-1.cdninstagram.com/t51.2885-15/e35/18380995_1812320002420325_1069760359251836928_n.jpg"

print(re.findall(regex,link))

r = requests.get("https://www.instagram.com/p/BNo2jsWj1-T/")



meh =re.findall(regex,r.text)

print(meh[0])