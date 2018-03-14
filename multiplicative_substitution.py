#Multiplicative substitution cipher
plainText = input("Enter plaintext:")
plainText = list(plainText)
cipherText = []
plainText = [ord(i)-96 for i in plainText]
key = 7
print("Key:",key)
for i in range(len(plainText)):
	if plainText[i] == 32-96:
		cipherText.append(chr(plainText[i]+96))
	elif ((plainText[i] * key) > 26):
		cipherText.append(chr(((plainText[i] * key) % 26) + 65))
	else:
		cipherText.append(chr(((plainText[i] * key)+65)))
print("Ciphertext: ",end="")
print(''.join(map(lambda x: str(x),cipherText)))