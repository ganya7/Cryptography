def swap(x,y):
    temp = x
    x = y
    y = temp
    return x,y

#==============================================================================
#                                 Encryption
#==============================================================================
def encrypt(p,k):
    c = []
    for i in range(0,len(p)):
        c.append(p[i]^k[i])
    print("Ciphertext: ",c)
    return c

#==============================================================================
#                                Decryption
#==============================================================================
def decrypt(c,k):
    p = []
    for i in range(0,len(c)):
        p.append(c[i]^k[i])
    print("Plaintext: ",p)

def main():
#==============================================================================
#                               Taking Input
#==============================================================================
    p = []
    plaintext = input("Enter the plaintext: ")
    temp1 = list(plaintext)
    for i in range(0,len(temp1)):
        p.append(int(temp1[i]))
    k = []
    key = input("Enter the key: ")
    temp2 = list(key)
    for i in range(0,len(temp2)):
        k.append(int(temp2[i]))

#==============================================================================
#                               Generating T and S
#==============================================================================
    s = []
    t = []
    for i in range(0,8):
        s.append(i)
        pos = i%len(k)
        t.append(k[pos])
        
#==============================================================================
#                          Initial Permutation of S
#==============================================================================
    j = 0
    for num in range(0,8):
        j = (j+s[num]+t[num])%8
        s[i],s[j] = swap(s[i],s[j])
    
#==============================================================================
#                            Stream Generation    
#==============================================================================
    i = 0
    j = 0
    keystream = []
    for num in range(0,len(p)):
        i = (i+1)%8
        j = (j+s[i])%8
        s[i],s[j] = swap(s[i],s[j])
        t = (s[i]+s[j])%8
        keystream.append(s[t])
    c = encrypt(p,keystream)
    decrypt(c,keystream)
    
if __name__ == '__main__':
    main()
    

