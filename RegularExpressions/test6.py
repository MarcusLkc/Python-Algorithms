import re

randStr = "<a href='#'><b>The Link</b></a>"

regex = re.compile(r"<a.*?>(.*?)</a>")

print(re.findall(regex,randStr))