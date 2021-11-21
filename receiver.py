import random
from elgamal import decrypt
from elgamal import q
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