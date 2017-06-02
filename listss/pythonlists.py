import random
import math

numlist = []

for i in range(5):
	numlist.append(random.randrange(1,10))

i = len(numlist) - 1
print(numlist)
while i > 1:

	j = 0

	while j < i:

		if numlist[j] > numlist[j+1]:

			numlist[j], numlist[j+1] = numlist[j+1], numlist[j]

		
		j += 1

	i -= 1

for k in numlist:
	print(k, end=",")
print()			