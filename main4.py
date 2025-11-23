import jwt;

try:
    key = "EstaEsLaContraseña";

    encoded = jwt.encode({"Usuario": "Test.jhsgdfhgdjh"}, key, algorithm="HS256");
    print(encoded);

    decoded = jwt.decode(encoded, key, algorithms="HS256");
    print(decoded);
    print(decoded["Usuario"]);
except Exception as ex:
    print(ex);

"""
py -m pip install PyJWT
"""