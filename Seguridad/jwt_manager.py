
import jwt
import datetime
import os

from Seguridad.aes_cipher import AESCipher

# Campos del payload que se cifran con AES dentro del token
AES_FIELDS = ["usuario_id", "rol", "cliente_id", "id_sucursal"]


class JWTManager:
    def __init__(self):
        self.secret = os.environ.get("JWT_SECRET_KEY")
        if self.secret is None:
            raise ValueError("¡La variable de entorno JWT_SECRET_KEY no está definida!")

        self.algorithm = "HS256"
        self.aes = AESCipher()

    def create_token(self, payload: dict) -> str:
        #expiración (2 horas )
        
        payload = payload.copy()

        for field in AES_FIELDS:
            if field in payload:
                payload[field] = self.aes.encrypt(str(payload[field]))

        payload.setdefault(
            "exp",
            datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        )

        token = jwt.encode(payload, self.secret, algorithm=self.algorithm)
        return token

    def verify_token(self, token: str) -> dict:    
        #Verifica firma, expiración y descifra campos sensibles.
        decoded = jwt.decode(token, self.secret, algorithms=[self.algorithm])

        for field in AES_FIELDS:
            if field in decoded:
                decoded[field] = self.aes.decrypt(decoded[field])

        return decoded
