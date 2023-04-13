from signing_module import *
import yaml

print('Curve:', curve.name)
message_file = "message.txt"
signature_file = "signature.yaml"
random.seed(42)     # fix randomness for demonstration

def author_signing():
    # encryption of message
    print("Author side")
    private, public = make_keypair()
    print("Private key:", hex(private))
    print("Public key: (0x{:x}, 0x{:x})".format(*public))

    with open(message_file, 'rb') as msg_file:
        msg = msg_file.read()
    signature = sign_message(private, msg)

    with open(signature_file, 'w') as file:
        yaml.dump({"measage file": message_file, 
                "public key": list(public), 
                "signature": list(signature)}, 
                file)

    print()
    print('Author checks his signature')
    print('Message:', msg)
    print('Signature: (0x{:x}, 0x{:x})'.format(*signature))
    print('Verification:', verify_signature(public, msg, signature))

def user_verification():
    print()
    print("User side")
    with open(signature_file, 'r') as file:
        sign_data = yaml.safe_load(file)
        
    message_file = sign_data["measage file"]
    public = tuple(sign_data["public key"])
    signature = tuple(sign_data["signature"])
    
    # correct message check
    print("User checks authors signature on correct message")

    with open(message_file, 'rb') as msg_file:
        msg = msg_file.read()
    print('Message:', msg)
    print('Verification:', verify_signature(public, msg, signature))

    # wrong message check
    print()
    print("User checks authors signature on wrong message")
    msg = b'Hi there!'
    print('Message:', msg)
    print('Verification:', verify_signature(public, msg, signature))

    print()
    print("User checks right message with wrong signaure")
    private, public = make_keypair()

    msg = b'Hello!'
    print('Message:', msg)
    print("Public key: (0x{:x}, 0x{:x})".format(*public))
    print('Verification:', verify_signature(public, msg, signature))


author_signing()

user_verification()