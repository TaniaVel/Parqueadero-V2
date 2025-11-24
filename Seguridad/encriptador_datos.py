from Seguridad.aes_cipher import AESCipher

aes = AESCipher()

#Recorre  diccionario (cliente) y cifra campos sensibles
SENSITIVE_FIELDS = ["Documento", "Correo", "Telefono", "Direccion"]

def encrypt_sensitive_fields(data: dict) -> dict:
    
    result = data.copy()

    for field in SENSITIVE_FIELDS:
        if field in result and result[field] is not None:
            try:
                result[field] = aes.encrypt(str(result[field]))
            except:
                pass

    return result

def encrypt_list(lista: list) -> list:
    return [encrypt_sensitive_fields(item) for item in lista]
