import re

phonelist = "412-555-1212 343 223 2342"

print(re.findall("\d{3}[\s-]\d{3}[\s-]\d{4}", phonelist))