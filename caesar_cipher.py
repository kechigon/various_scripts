str = "any encoded string"
for i in range(1, 26):
	tmp = ''
	for j in range(len(str)):
		if ord('A') <= ord(str[j]) and ord(str[j]) <= ord('Z'):
			if ord(str[j]) + i > 90:
				tmp += chr(64 + (ord(str[j]) + i - 90))
			else:
				tmp += chr(ord(str[j]) + i)
		elif ord('a') <= ord(str[j]) and ord(str[j]) <= ord('z'):
			if ord(str[j]) + i > 122:
				tmp += chr(96 + (ord(str[j]) + i - 122))
			else:
				tmp += chr(ord(str[j]) + i)
		else:
			tmp += str[j]
	print(tmp)
	print('')
