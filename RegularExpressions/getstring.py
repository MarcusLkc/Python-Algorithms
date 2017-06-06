import re 

randstr = "@ Get this string"

regex = re.compile(r"[^@\s].*$")

print(re.findall(regex, randstr))



# lazy and greedy