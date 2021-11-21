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


class EncriptedMessageInfo:
    def __init__(self, encripted_msg, p) -> None:
        self.message= encripted_msg
        self.p = p


class Sender():
    def __init__(self) -> None:
        self.messages = plain_messages
        self.private_keys = []
        self.encripted_messages_info = []
    
    
    def createPrivateKeys(self):
        for _ in self.messages:
            new_private_key = gen_key(q)
            self.private_keys.append(new_private_key)
    
    
    def returnPrivateKey(self, i):
        return self.private_keys[i]  


    def returnEncriptedMessages(self):
        return self.encripted_messages_info
    
    
    def encrypt(self, public_keys):
        for i, public_key in enumerate(public_keys):

            msg = self.messages[i]

            h = power(public_key, self.private_keys[i], q)

            en_msg, p = encrypt(msg, h, public_key)
            new_enc_msg = EncriptedMessageInfo(en_msg, p)
            self.encripted_messages_info.append(new_enc_msg)
        return new_enc_msg



class Receiver():
       def __init__(self) -> None:
           self.public_keys = []
           self.private_key = None
           self.encripted_message_info = None
        
       def createPublicKeys(self):
            g = random.randint(2, q)    
            g2 = random.randint(2, q)
            g3 = random.randint(2, q)
            self.public_keys = [g, g2, g3]
        
       def savePrivateKey(self, private_key):
            self.private_key = private_key

       def sendPublicKeys(self):
            return self.public_keys
        
       def decrypt(self, encripted_messages):
           for enc_msg in encripted_messages:
               message = enc_msg.message
               p = enc_msg.p
               decripted_message = decrypt(message, p, self.private_key)
               dmsg = ''.join(decripted_message)
               print("Decrypted Message :", dmsg)
       

def main():

    sender = Sender()

    receiver = Receiver()
    
    sender.createPrivateKeys()
    
    receiver.createPublicKeys()

    public_keys = receiver.sendPublicKeys()

    sender.encrypt(public_keys)

    private_key = sender.returnPrivateKey(1)

    receiver.savePrivateKey(private_key)

    encripted_messages = sender.returnEncriptedMessages()

    receiver.decrypt(encripted_messages)

if __name__ == '__main__':
    main()