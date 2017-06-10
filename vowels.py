# Paste your code into this box 
s = 'paypvtsaxsvkvnjsuw'
longestword = ""
currentword = ""
s += s[len(s)-1]
for i in range (len(s)-1):
    
    if(s[i]<=s[i+1]):
        currentword += s[i]

    else:
        currentword += s[i]
        if len(currentword) > len(longestword):
            longestword = currentword

        currentword = ""
if len(currentword) > len(longestword):
	longestword = currentword


print("longest substring in alphabetical order is: ",longestword)
    