# Cryptography 3.1
import random
import Crypto.Util.number as cu

# Exercise 1

def GCD(a, b) :
    while True :
        temp = a % b
        if (temp == 0) :
            return b
        a = b
        b = temp


def calculateNPQ() :
    n,p,q = 1,1,1
    while (n.bit_length() < 2048 or p == q) :
        p = cu.getPrime(1152)
        q = cu.getPrime(1024)
        n = p * q
        # print(n.bit_length())
    return n,p,q


def calculateF(p,q) :
    f = (p - 1) * (q - 1)
    return f

def calculateE(f) :
    e = 2
    while not (cu.GCD(f,e) == 1 and e.bit_length() > 512) :
        e = random.randint(1,f)
    return e


def extendedGCD(a, b):
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y



def RSAEncode(m,e,n) :
    byte_array = bytearray(m.encode())
    long_array = []
    encoded = cu.bytes_to_long(byte_array)
    encoded = pow(encoded,e,n)
    return encoded


def calculateD(e,fi):
    gcd, x, y = extendedGCD(e, fi)
    if (x < 0):
        d = x + fi
    else:
        d = x
    return d


def RSADecode(crypto,d,n) :
    longe = pow(crypto, d, n)
    byte_array = cu.long_to_bytes(longe)
    print(byte_array)
    message = str(byte_array)
    return message


n,p,q = calculateNPQ()
fi = calculateF(p,q)
e = calculateE(fi)
d = calculateD(e,fi)
m = "jose"

cryptogram = RSAEncode(m,e,n)
decoded = RSADecode(cryptogram,d,n)
print("N is : ",n)
print("P is : ",p)
print("Q is : ",q)
print("F is : ",fi)
print("E is : ",e)
print("D is : ",d)
print("m is : ",m)
print("cryptogram is : ",cryptogram)
print("cryptogram decoded is : ",decoded)
