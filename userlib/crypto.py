# from base58 import b58encode, b58decode
# import ujson
# from Cryptodome.Cipher import AES
# from Cryptodome.Random import get_random_bytes

# def gen_key():
#     return get_random_bytes(16)


# JSK = ['nonce', 'header', 'ciphertext', 'tag']

# class Crypter:
#     def __init__(self, token, header='re'):
#         self.token = token.encode()
#         self.header = header.encode()

#     def encode(self, msg):
#         data = ujson.dumps(msg).encode()
#         cipher = AES.new(self.token, AES.MODE_EAX)
#         cipher.update(self.header)
#         ciphertext, tag = cipher.encrypt_and_digest(data)

#         return ".".join([b58encode(x).decode('utf-8') for x in (cipher.nonce, self.header, ciphertext, tag,)])

#     def decode(self, str):

#         obj = dict(zip(JSK, [b58decode(x) for x in str.split('.')]))
#         cipher = AES.new(self.token, AES.MODE_EAX, nonce=obj['nonce'])
#         cipher.update(obj['header'])
#         plaintext = cipher.decrypt(obj['ciphertext'])

#         return ujson.loads(plaintext)
