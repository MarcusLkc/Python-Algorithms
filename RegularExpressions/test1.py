import re

hair = " rat cat mat pat"

regex = re.compile("[cr]at")

hair = regex.sub("owl", hair)

print(hair)
