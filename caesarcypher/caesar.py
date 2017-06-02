def crypt(message, key):
	new_message = ""

	#loop through the message
	for char in message:
			#check to see if character is alphabet
		if char.isalpha():
			#if char is alpha turn it into unicode then add key value
			char_code = ord(char)
			char_code += key
			#check if char is uppercase
			if char.isupper():
			#if char is uppercase alter value to fit into character range
				if char_code > ord('Z'):
					char_code -= 26

				if char_code < ord('A'):
					char_code += 26

			else:
			#same for if character code ends up being outside the range of a and z
				if char_code > ord('z'):
					char_code -= 26

				if char_code < ord('a'):
					char_code += 26
			new_message += chr(char_code)
		#if char isnt alpha just add it for things such as spaces
		else:
			new_message += char
	
	return new_message
	


secret_message = ""

message = input("Enter your message: ")
key = int(input("How many characters should we shift (1-26) "))
secret_message = crypt(message, key)
print(f'Encrypted {secret_message}')
key = -key
crypt
orig_message = crypt(secret_message, key)

print(orig_message)