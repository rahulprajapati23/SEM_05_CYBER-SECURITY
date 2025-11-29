import pytest
from cryptography.fernet import Fernet

# test_pass.py


# Refactored logic from pass.py for testing
def encrypt_password(password: str, key: bytes) -> bytes:
    cipher = Fernet(key)
    return cipher.encrypt(password.encode())

def decrypt_password(encrypted: bytes, key: bytes) -> str:
    cipher = Fernet(key)
    return cipher.decrypt(encrypted).decode()

def test_encryption_and_decryption():
    key = Fernet.generate_key()
    password = "TestPassword123"
    encrypted = encrypt_password(password, key)
    assert isinstance(encrypted, bytes)
    decrypted = decrypt_password(encrypted, key)
    assert decrypted == password