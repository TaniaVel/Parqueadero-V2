
'''
Esta clase se encarga de tomar los datos (ejemp correo, documento), y los converter
 en un texto incomprensible mediante el algoritmo de cifrado  AES.
También puede hacer lo contrario: recibir ese texto cifrado y devolver el dato original.
Se usa una clave secreta que sólo el servidor conoce, así  nadie más puede leer
 la información.
'''

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

class AESCipher:
    def __init__(self, key=None):
        
        #La clave se toma desde la variable de entorno AES_SECRET_KEY.
    
        secret_key = key or os.environ.get("AES_SECRET_KEY")

        if secret_key is None:
            raise ValueError("La variable de entorno AES_SECRET_KEY no está definida")

        key_bytes = secret_key.encode("utf-8")

        if len(key_bytes) not in (16, 24, 32):
            raise ValueError(
                f"La clave AES_SECRET_KEY debe tener 16, 24 o 32 caracteres. Longitud actual: {len(key_bytes)}"
            )

        self.key = key_bytes
        self.bs = AES.block_size 

    def encrypt(self, raw: str) -> str:
        
        #Recibe un texto normal y devuelve el texto cifrado en Base64.
        
        raw_bytes = raw.encode("utf-8")
        iv = os.urandom(self.bs)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(pad(raw_bytes, self.bs))
        return base64.b64encode(iv + encrypted).decode("utf-8")

    def decrypt(self, enc: str) -> str:
        #Recibe un texto cifrado en Base64 y devuelve el texto original.
        enc_bytes = base64.b64decode(enc)
        iv = enc_bytes[:self.bs]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(enc_bytes[self.bs:]), self.bs)
        return decrypted.decode("utf-8")
