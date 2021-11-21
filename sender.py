from elgamal import q, plain_messages, power, gen_key, encrypt
from encriptedMessageInfo import EncriptedMessageInfo
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
