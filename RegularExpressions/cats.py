import re 

randstr = "My number is 412-555-1214"

regex = re.compile(r"412-(.*)-(.*)")

matches =re.findall(regex, randstr)

print(matches[0][0])



# lazy and greedy