"""
Librerias: 

py -m pip install pyodbc
py -m pip install Flask
py -m pip install jsonify

"""  

import flask
import json
from Repositorios.Cone_Cliente import Conexion_Cliente

app = flask.Flask(__name__)

@app.route('/main3/Cargarclientes/<string:entrada>', methods=["GET"])
def CargarClientes(entrada: str) -> str:
    respuesta: dict = {}

    try:
       
        entrada = entrada.replace("'", '"')
        datos_entrada = json.loads(entrada)
        respuesta["Entrada"] = datos_entrada

        conexion = Conexion_Cliente()
        lista_clientes = conexion.CargarClientes()

        # Preparar respuesta JSON
        clientes_json = {}
        contador = 0

        for cli in lista_clientes:
            temp = {
                "IdCliente": cli.GetIdCliente(),
                "Nombre": cli.GetNombre(),
                "Documento": cli.GetDocumento(),
                "Telefono": cli.GetTelefono(),
                "Correo": cli.GetCorreo(),
                "Direccion": cli.GetDireccion()
            }
            clientes_json[str(contador)] = temp
            contador += 1

        respuesta["Clientes"] = clientes_json
        respuesta["Respuesta"] = "OK"

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Error"] = str(ex)
        respuesta["Respuesta"] = "Error"
        return flask.jsonify(respuesta)


app.run('localhost', 4040)
