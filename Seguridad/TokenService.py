from flask import jsonify
from Seguridad.jwt_manager import JWTManager

class TokenService:
    def __init__(self):
        self.jwt = JWTManager()

    def generar_token(self, payload: dict):

        if not payload or not isinstance(payload, dict):
            return jsonify({"Error": "Debes enviar un JSON con los datos del token"}), 400

        try:
            token = self.jwt.create_token(payload)

            return jsonify({
                "mensaje": "Token generado correctamente",
                "token": token,
                "payload_recibido": payload
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500
