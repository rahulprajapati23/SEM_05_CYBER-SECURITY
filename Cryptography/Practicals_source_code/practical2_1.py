import hashlib
passwd = input("Enter password: ")

encoded_passwd = passwd.encode('utf-8')
hashed_passwd = hashlib.sha512(encoded_passwd).hexdigest()

print(f"Original password (encoded): {encoded_passwd}")
print(f"Hashed password (md5): {hashed_passwd}")

usr_passwd = input("Re-enter password: ")

if hashlib.sha512(usr_passwd.encode('utf-8')).hexdigest() == hashed_passwd:
    print("hash matched successfully")
    print(f"decrypted password:{usr_passwd}")
else:
    print("Password does not match.")