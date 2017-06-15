import requests, os, bs4
import re
import webbrowser
from urllib.request import urlretrieve

os.makedirs('insta', exist_ok=True)
r = requests.get("https://www.instagram.com/p/BPV6UIFguCL/?taken-by=mkclegacy")

soup = bs4.BeautifulSoup(r.text, "html.parser")

mydivs = soup.find("meta", { "property" : "og:image" })
url = mydivs.get('content')
res = requests.get(url)

urlretrieve(url, "wof.svg")

imageFile = open(os.path.join('insta', os.path.basename(url)), 'wb') 
for chunk in res.iter_content(100000):
	imageFile.write(chunk)
imageFile.close()






