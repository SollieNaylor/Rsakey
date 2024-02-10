

import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def generate_keys(bit_length):
    p = generate_prime(bit_length)
    q = generate_prime(bit_length)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break
    
    d = mod_inverse(e, phi)
    
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(cipher, private_key):
    d, n = private_key
    message = ''.join([chr(pow(char, d, n)) for char in cipher])
    return message

def sign(message, private_key):
    d, n = private_key
    signature = [pow(ord(char), d, n) for char in message]
    return signature

def authenticate(signature, message, public_key):
    e, n = public_key
    reconstructed_message = ''.join([chr(pow(char, e, n)) for char in signature])
    return reconstructed_message == message

def main():
    print("RSA keys are being generated...")
    public_key, private_key = generate_keys(16)
    print("RSA keys have been generated.")

    while True:
        print("Please select your user type:")
        print("1. A public user")
        print("2. The owner of the keys")
        print("3. Exit program")

        user_type = int(input("Enter your choice: "))

        if user_type == 1:
            print("As a public user, what would you like to do?")
            print("1. Send an encrypted message")
            print("2. Authenticate a digital signature")
            print("3. Exit")

            public_choice = int(input("Enter your choice: "))

            if public_choice == 1:
                message = input("Enter a message: ")
                cipher = encrypt(message, public_key)
                print("Message encrypted and sent.")
            elif public_choice == 2:
                if 'signature' not in locals():
                    print("There are no signatures to authenticate.")
                else:
                    original_message = input("Enter the original message: ")
                    if authenticate(signature, original_message, public_key):
                        print("Signature is valid.")
                    else:
                        print("Signature is not valid.")
            elif public_choice == 3:
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")

        elif user_type == 2:
            print("As the owner of the keys, what would you like to do?")
            print("1. Decrypt a received message")
            print("2. Digitally sign a message")
            print("3. Show the keys")
            print("4. Generate a new set of keys")
            print("5. Exit")

            owner_choice = int(input("Enter your choice: "))

            if owner_choice == 1:
                if 'cipher' not in locals():
                    print("There are no messages to decrypt.")
                else:
                    decrypted_message = decrypt(cipher, private_key)
                    print("Decrypted message:", decrypted_message)
            elif owner_choice == 2:
                message_to_sign = input("Enter a message: ")
                signature = sign(message_to_sign, private_key)
                print("Message signed and sent.")
            elif owner_choice == 3:
                print("Public Key:", public_key)
                print("Private Key:", private_key)
            elif owner_choice == 4:
                print("Generating new RSA keys...")
                public_key, private_key = generate_keys(16)
                print("New RSA keys have been generated.")
            elif owner_choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")
        elif user_type == 3:
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

