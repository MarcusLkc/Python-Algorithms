import re 

randStr = "https://www.youtube.com http://www.google.com"


regex = re.compile(r"(https?://(.+?m))")

randStr = re.sub(regex, r"<a href=\1>\2</a>\n", randStr)

#re.compile(r"(https?://([\w]+))")


print(randStr)