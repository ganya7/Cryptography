import random

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

p = int(input("Enter a prime number (modulus): "))
if not (is_prime(p)):
        raise ValueError('Number must be prime.')
else:
	a = int(input("Enter Alice private key:"))
	b = int(input("Enter Bob private key:"))
	g = []
	h = []
	for i in range(1,p):
		for j in range(1,p):
			h.append(pow(i, j, p)) 
		if h.count(1) <= 1:
			g.append(i)
		h=[]
	print("Primitve roots of p (modulus): ",g)
	primitive_root = g[random.randrange(0,len(g))]
	print("Primitive root (Generator g): ",primitive_root)
	publicKey_Alice = (primitive_root**a) % p
	publicKey_Bob = (primitive_root**b) % p
	encryptionKey = (primitive_root**(a*b)) % p
	print("Alice: Private key: ",a," Public key: ",publicKey_Alice,end=" ")
	print("(",a,", ",publicKey_Alice,")")
	print("Bob: Private key: ",b," Public key: ",publicKey_Bob,end=" ")
	print("(",b,", ",publicKey_Bob,")")
	print("Encryption key: ",encryptionKey)
	cAlice = ((primitive_root**a)**b) % p
	cBob = ((primitive_root**b)**a) % p
	print("Alice calculate value with Bob's key: ",cAlice)
	print("Bob calculate value with Alice's key: ",cBob)
	if cAlice == cBob:
		print("They are equal")