'''import hashlib
import binascii, os
from Crypto.Cipher import AES

class EncriptarMD5:
    def Executar(self) -> None :
        valor = "Solter@s";
        print("Value: " + valor);
        resutlado = self.Encriptar(valor);
        print("Encrypt: " + resutlado);
        
    def Encriptar(self, valor: str) -> str :
        return str(hashlib.md5(valor.encode('utf-8')).hexdigest());

    def Descifrar(self, valor: str) -> str :
        return None;

class EncriptarAES1:
    secretKey = b'4563265512345678';

    def Executar(self) -> None :
        valor = "Solter@s";
        print("Value: " + valor);
        resultado = self.Encriptar(valor);
        print("Encrypt: " + resultado);

        resultado = self.Descifrar(resultado);
        print("Decrypt: " + resultado);
        
    def Encriptar(self, valor: str) -> str :
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM);
        ciphertext, authTag = aesCipher.encrypt_and_digest(str.encode(valor));
        response = (ciphertext, aesCipher.nonce, authTag);
        return binascii.hexlify(response[0]).decode() + '|' + binascii.hexlify(response[1]).decode() + '|' + binascii.hexlify(response[2]).decode();

    def Descifrar(self, valor: str) -> str :
        split = valor.split('|');
        ciphertext = binascii.unhexlify(split[0]);
        nonce = binascii.unhexlify(split[1]);
        authTag = binascii.unhexlify(split[2]);
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce);
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag);
        return plaintext.decode();

print("MD5---------------------------");
test = EncriptarMD5();
test.Executar();

print("AES---------------------------");
test = EncriptarAES1();
test.Executar();

"""
py -m pip install pycryptodome
"""

'''