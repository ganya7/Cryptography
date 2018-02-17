import random

def gcd(a,b):
    if (a == 0):
        return b
    return gcd(b%a, a)

def multiplicative_inverse(e, phi):
    for i in range(phi):
        d = i
        if (d * e) % phi == 1:
            break
    return d

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p-1) * (q-1)
    # e = 2
    # g = gcd(e,phi)
    # while g != 1:
    #     e += 1
    #     g = gcd(e, phi)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    print("Public key: ",e)

    d = multiplicative_inverse(e, phi)
    print("Private key: ",d)
    return ((e, n), (d, n))

def encrypt(privateKey, plaintext):
    key, n = privateKey
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(privateKey, ciphertext):
    key, n = privateKey
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)
    
def main():
    print ("RSA Encrypter/ Decrypter")
    p,q = map(int,input("Enter p and q (should be prime and large number,17, 19, 23, etc): ").split())
    public, private = generate_keypair(p, q)
    print ("Your public key is ", public ," and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print ("Your encrypted message is: ")
    print (''.join(map(lambda x: str(x), encrypted_msg)))
    print ("Decrypting message with public key ", public ," . . .")
    print ("Your message is:")
    print (decrypt(public, encrypted_msg))

main()