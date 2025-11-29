from cryptography.fernet import Fernet
import getpass

key = Fernet.generate_key()
cipher = Fernet(key)

password = input("Enter your password: ").encode()

encrypted = cipher.encrypt(password)
print(" Encrypted password:", encrypted)

decrypted = cipher.decrypt(encrypted)
print(" Decrypted password:", decrypted.decode())