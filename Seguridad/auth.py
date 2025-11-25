#se encarga de revisar si la persona que está intentando usar la API tiene un token válido.

from functools import wraps
from flask import request, jsonify

from Seguridad.jwt_manager import JWTManager

jwt_manager = JWTManager()

#Es el que  permite el acceso si el usuario envía un token válido.
def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # En el postman en Header quedaría así: Authorization: Bearer <token>
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.replace("Bearer ", "", 1)
            else:
                token = auth_header

        # Si no llega token, no permitimos el acceso
        if not token:
            return jsonify({"error": "Token faltante"}), 401

        try:
            data = jwt_manager.verify_token(token)
            request.user = data
        except Exception as e:
            return jsonify({"error": "Token inválido: " + str(e)}), 401

        return f(*args, **kwargs)

    return decorated
