import random
from math import pow


# we choose a random very large number q
q = random.randint(pow(10, 20), pow(10, 50))
plain_messages = ["first", "second", "third"]

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# Generating large random numbers
def gen_key(q):
	key = random.randint(pow(10, 20), q)
	while gcd(q, key) != 1:
		key = random.randint(pow(10, 20), q)

	return key


# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a
    
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    
    return x % c


# Asymmetric encryption
def encrypt(msg, h, g):
    
    en_msg = []
    
    k = gen_key(q)# Private key for sender

    # AKA g^k
    p = power(g, k, q)

    # AKA g^ak
    s = power(h, k, q)


    for i in range(0, len(msg)):
	    en_msg.append(msg[i])

    for i in range(0, len(en_msg)):
	    en_msg[i] = s * ord(en_msg[i])

    return en_msg, p


def decrypt(en_msg, p, key):

	dr_msg = []
	h = power(p, key, q)
	for i in range(0, len(en_msg)):
		dr_msg.append(chr(int(en_msg[i]/h)))
		
	return dr_msg