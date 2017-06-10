import requests, os, bs4
import re
import webbrowser
from urllib.request import urlretrieve

os.makedirs('instasave', exist_ok=True)
r = requests.get("https://www.instagram.com/p/BMIKKMuAmQH/?taken-by=mkclegacy")

soup = bs4.BeautifulSoup(r.text, "html.parser")

mydivs = soup.find("meta", { "property" : "og:image" })

res = requests.get(mydivs.get('content'))



imageFile = open(os.path.join('instasave', os.path.basename("hooty5")), 'wb')

urlretrieve(str(mydivs.get('content')), "me.jpg")


new = 2




