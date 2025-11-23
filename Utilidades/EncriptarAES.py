import hashlib
import binascii, os
from Crypto.Cipher import AES

class EncriptarAES:
    secretKey = b'4563265512345678';
    
    def Encriptar(self, value: str) -> str :
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM);
        ciphertext, authTag = aesCipher.encrypt_and_digest(str.encode(value));
        return (ciphertext, aesCipher.nonce, authTag);

    def Descifrar(self, value: str) -> str :
        (ciphertext, nonce, authTag) = value;
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce);
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag);
        return plaintext;