def caesar_cipher_encryption(plainText,n):
  cipherText = None
  cipherText = list(plainText)
  for i in range(len(cipherText)):
  #cipherText[i] = chr(ord(cipherText[i]) + n)
    if (ord(cipherText[i])+n) > 122:
      cipherText[i] = chr(ord(cipherText[i]) + n - 26)
    else:
      cipherText[i] = chr(ord(cipherText[i]) + n)
  cipherText = ''.join(cipherText)
  print("Cipher text is: ",cipherText.upper())
  cipherText = cipherText.upper()
  key_d = int(input("Enter key for decryption: "))
  caesar_cipher_decryption(cipherText,key_d)

def caesar_cipher_decryption(cText,n):
  pText = None
  pText = list(cText)
  #print(pText)
  #print(pText[0])
  #print(ord(pText[0]))
  for i in range(len(pText)):
    if (ord(pText[i]) - n) < 65:
      pText[i] = chr(ord(pText[i]) - n + 26)
    else:
      pText[i] = chr(ord(pText[i]) - n)
  pText = ''.join(pText)
  print("Decrypted text: ",pText.lower())
pText = input("Enter plainText: ")
key = int(input("Enter key: "))
caesar_cipher_encryption(pText,key)