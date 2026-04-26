import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

text = "test£"
key = os.urandom(32)
nonce = os.urandom(12)
cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
encryptor = cipher.encryptor()
ct = encryptor.update(text.encode('utf-8')) + encryptor.finalize()
ciphertext = ct + encryptor.tag
encrypted = base64.b64encode(key).decode() + ':' + base64.b64encode(nonce).decode() + ':' + base64.b64encode(ciphertext).decode()
print("Encrypted: " + encrypted)