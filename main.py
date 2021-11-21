from sender import Sender
from receiver import Receiver
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