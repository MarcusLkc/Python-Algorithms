import re

if re.search("\w{2,20}\s{1-4}\w{2,20}", "Toshio   Muramatsa"):
	print("It is valid")