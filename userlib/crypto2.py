import cryptography
from cryptography.fernet import Fernet
import ujson

class SimpleCrypt:
    def __init__(self, key):
        self.key = key
        self.f = Fernet(key)

    def encrypt(self, struct):
        enc_data = ujson.dumps(struct)
        encrypted = self.f.encrypt(enc_data)
        return encrypted.decode()

    def decrypt(self, raw):
        decrypted = self.f.decrypt(raw)
        struct = ujson.loads(decrypted).decode()
        return struct

