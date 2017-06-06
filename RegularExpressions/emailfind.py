import re

emailList = "db@aol.com m@.com @apple.com db@.com w.a@gmail.com"
print(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}\.[A-Za-z]{2,3}", emailList))