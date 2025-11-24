# app.py

import flask
import json
from Seguridad.auth import token_required
from Seguridad.TokenService import TokenService

from Servicios.Servicio_Cliente import Servicio_Cliente
from Servicios.Servicio_Vehiculo import Servicio_Vehiculo
from Servicios.Servicio_Empleado import Servicio_Empleado
from Servicios.Servicio_RolEmpleado import Servicio_RolEmpleado
from Servicios.Servicio_TipoVehiculo import Servicio_TipoVehiculo
from Servicios.Servicio_Tarifa import Servicio_Tarifa
from Servicios.Servicio_EntradaSalida import Servicio_EntradaSalida
from Servicios.Servicio_MetodoPago import Servicio_MetodoPago
from Servicios.Servicio_Pago import Servicio_Pago
from Servicios.Servicio_Factura import Servicio_Factura
from Servicios.Servicio_Gasto import Servicio_Gasto
from Servicios.Servicio_Multa import Servicio_Multa
from Servicios.Servicio_Incidente import Servicio_Incidente
from Servicios.Servicio_Membresia import Servicio_Membresia
from Servicios.Servicio_Promocion import Servicio_Promocion


app = flask.Flask(__name__)

# =========================================
# Endpoint para generar TOKEN de ADMIN
# =========================================

token_service = TokenService()

#Generar el token

@app.route("/token/generar", methods=["POST"])
def generar_token():
    payload = flask.request.json
    return token_service.generar_token(payload)

#  GET - Cargar clientes
@app.route("/main3/Cargarclientes/<string:entrada>", methods=["GET"])
def api_cargar_clientes(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Cliente()
        respuesta["Clientes"] = servicio.CargarClientes()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)


# GET - Cargar clientes -con datos sensibles encriptados
@app.route("/main3/Cargarclientes2/<string:entrada>", methods=["GET"])
def api_cargar_clientes2(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Cliente()
        respuesta["Clientes"] = servicio.CargarClientes2()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)
    

# POST - Insertar cliente
@app.route("/main3/InsertarCliente", methods=["POST"])
def api_insertar_cliente():

    datos = flask.request.json
    servicio = Servicio_Cliente()
    mensaje = servicio.InsertarCliente(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar cliente
@app.route("/main3/ActualizarCliente", methods=["PUT"])
def api_actualizar_cliente():

    datos = flask.request.json
    servicio = Servicio_Cliente()
    mensaje = servicio.ActualizarCliente(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar cliente
@app.route("/main3/EliminarCliente/<int:id_cliente>", methods=["DELETE"])
def api_eliminar_cliente(id_cliente: int):

    servicio = Servicio_Cliente()
    mensaje = servicio.EliminarCliente(id_cliente)

    return flask.jsonify({"Respuesta": mensaje})
# ===========================================================
# VEHÍCULO
# ===========================================================

# GET - Cargar vehículos
@app.route("/main3/CargarVehiculos/<string:entrada>", methods=["GET"])
def api_cargar_vehiculos(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Vehiculo()
        respuesta["Vehiculos"] = servicio.CargarVehiculos()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# POST - Insertar vehículo
@app.route("/main3/InsertarVehiculo", methods=["POST"])
def api_insertar_vehiculo():

    datos = flask.request.json
    servicio = Servicio_Vehiculo()
    mensaje = servicio.InsertarVehiculo(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar vehículo
@app.route("/main3/ActualizarVehiculo", methods=["PUT"])
def api_actualizar_vehiculo():

    datos = flask.request.json
    servicio = Servicio_Vehiculo()
    mensaje = servicio.ActualizarVehiculo(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar vehículo
@app.route("/main3/EliminarVehiculo/<int:id_vehiculo>", methods=["DELETE"])
def api_eliminar_vehiculo(id_vehiculo: int):

    servicio = Servicio_Vehiculo()
    mensaje = servicio.EliminarVehiculo(id_vehiculo)

    return flask.jsonify({"Respuesta": mensaje})

# ===========================================================
# TIPO VEHÍCULO
# ===========================================================

from Servicios.Servicio_TipoVehiculo import Servicio_TipoVehiculo

@app.route("/main3/CargarTipoVehiculo/<string:entrada>", methods=["GET"])
def api_cargar_tipovehiculo(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_TipoVehiculo()
        respuesta["TipoVehiculo"] = servicio.CargarTipoVehiculos()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# POST - Insertar vehículo
@app.route("/main3/InsertarTipoVehiculo", methods=["POST"])
def api_insertar_tipovehiculo():

    datos = flask.request.json
    servicio = Servicio_TipoVehiculo()
    mensaje = servicio.InsertarTipoVehiculo(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar vehículo
@app.route("/main3/ActualizarTipoVehiculo", methods=["PUT"])
def api_actualizar_tipovehiculo():

    datos = flask.request.json
    servicio = Servicio_TipoVehiculo()
    mensaje = servicio.ActualizarTipoVehiculo(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar vehículo
@app.route("/main3/EliminarTipoVehiculo/<int:id_tipo>", methods=["DELETE"])
def api_eliminar_tipovehiculo(id_tipo: int):

    servicio = Servicio_TipoVehiculo()
    mensaje = servicio.EliminarTipoVehiculo(id_tipo)

    return flask.jsonify({"Respuesta": mensaje})


# ===========================================================
# EMPLEADO
# ===========================================================

#GET - Cargar listado de empleados
@app.route("/main3/CargarEmpleados/<string:entrada>", methods=["GET"])
def api_cargar_empleados(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Empleado()
        respuesta["Empleados"] = servicio.CargarEmpleados()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# POST - Insertar empleado
@app.route("/main3/InsertarEmpleado", methods=["POST"])
def api_insertar_empleado():

    datos = flask.request.json
    servicio = Servicio_Empleado()
    mensaje = servicio.InsertarEmpleado(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar empleado
@app.route("/main3/ActualizarEmpleado", methods=["PUT"])
def api_actualizar_empleado():

    datos = flask.request.json
    servicio = Servicio_Empleado()
    mensaje = servicio.ActualizarEmpleado(datos)

    return flask.jsonify({"Respuesta": mensaje})

#  DELETE - Eliminar empleado
@app.route("/main3/EliminarEmpleado/<int:id_empleado>", methods=["DELETE"])
def api_eliminar_empleado(id_empleado: int):

    servicio = Servicio_Empleado()
    mensaje = servicio.EliminarEmpleado(id_empleado)

    return flask.jsonify({"Respuesta": mensaje})

# ===========================================================
# ROL EMPLEADO
# ===========================================================

#GET - Cargar lista de roles de empleado
@app.route("/main3/CargarRolEmpl/<string:entrada>", methods=["GET"])
def api_cargar_roles(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_RolEmpleado()
        respuesta["Roles"] = servicio.CargarRoles()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)
    

# POST - Insertar rol de empleado
@app.route("/main3/InsertarRolEmpl", methods=["POST"])
def api_insertar_rol():

    datos = flask.request.json
    servicio = Servicio_RolEmpleado()
    mensaje = servicio.InsertarRol(datos)

    return flask.jsonify({"Respuesta": mensaje})

#  PUT - Actualizar rol
@app.route("/main3/ActualizarRolEmpl", methods=["PUT"])
def api_actualizar_rol():

    datos = flask.request.json
    servicio = Servicio_RolEmpleado()
    mensaje = servicio.ActualizarRol(datos)

    return flask.jsonify({"Respuesta": mensaje})

#  DELETE - Eliminar rol
@app.route("/main3/EliminarRolEmpl/<int:id_rol>", methods=["DELETE"])
def api_eliminar_rol(id_rol: int):

    servicio = Servicio_RolEmpleado()
    mensaje = servicio.EliminarRol(id_rol)

    return flask.jsonify({"Respuesta": mensaje})


# ===========================================================
#  TARIFA
# ===========================================================

#GET - Cargar lista de tarifas
@app.route("/main3/CargarTarifas/<string:entrada>", methods=["GET"])
def api_cargar_tarifas(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Tarifa()
        respuesta["Tarifas"] = servicio.CargarTarifas()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

#GET - Cargar lista de tarifas
@app.route("/main3/InsertarTarifa", methods=["POST"])
def api_insertar_tarifa():

    datos = flask.request.json
    servicio = Servicio_Tarifa()
    mensaje = servicio.InsertarTarifa(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar tarifa
@app.route("/main3/ActualizarTarifa", methods=["PUT"])
def api_actualizar_tarifa():

    datos = flask.request.json
    servicio = Servicio_Tarifa()
    mensaje = servicio.ActualizarTarifa(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar tarifa
@app.route("/main3/EliminarTarifa/<int:id_tarifa>", methods=["DELETE"])
def api_eliminar_tarifa(id_tarifa: int):

    servicio = Servicio_Tarifa()
    mensaje = servicio.EliminarTarifa(id_tarifa)

    return flask.jsonify({"Respuesta": mensaje})


# ===========================================================
#  ENTRADA / SALIDA
# ===========================================================

# GET - Cargar lista de registros

@app.route("/main3/CargarEntradaSalida/<string:entrada>", methods=["GET"])
def api_cargar_entradasalida(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_EntradaSalida()
        respuesta["EntradaSalida"] = servicio.CargarRegistros()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# POST - Insertar registro
@app.route("/main3/InsertarEntrada", methods=["POST"])
def api_insertar_entrada():

    datos = flask.request.json
    servicio = Servicio_EntradaSalida()
    mensaje = servicio.InsertarRegistro(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar registro
@app.route("/main3/ActualizarEntradaSalida", methods=["PUT"])
def api_actualizar_entradasalida():

    datos = flask.request.json
    servicio = Servicio_EntradaSalida()
    mensaje = servicio.ActualizarRegistro(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar registro
@app.route("/main3/EliminarEntradaSalida/<int:id_registro>", methods=["DELETE"])
def api_eliminar_entradasalida(id_registro: int):

    servicio = Servicio_EntradaSalida()
    mensaje = servicio.EliminarRegistro(id_registro)

    return flask.jsonify({"Respuesta": mensaje})

# ===========================================================
#  METODO DE PAGO
# ===========================================================

# GET - Cargar métodos de pago
@app.route("/main3/CargarMetodos/<string:entrada>", methods=["GET"])
def api_cargar_metodos(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_MetodoPago()
        respuesta["Metodos"] = servicio.CargarMetodos()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# GET - Cargar métodos de pago
@app.route("/main3/InsertarMetodo", methods=["POST"])
def api_insertar_metodo():

    datos = flask.request.json
    servicio = Servicio_MetodoPago()
    mensaje = servicio.InsertarMetodo(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar método
@app.route("/main3/ActualizarMetodo", methods=["PUT"])
def api_actualizar_metodo():

    datos = flask.request.json
    servicio = Servicio_MetodoPago()
    mensaje = servicio.ActualizarMetodo(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar método
@app.route("/main3/EliminarMetodo/<int:id_metodo>", methods=["DELETE"])
def api_eliminar_metodo(id_metodo: int):

    servicio = Servicio_MetodoPago()
    mensaje = servicio.EliminarMetodo(id_metodo)

    return flask.jsonify({"Respuesta": mensaje})

# ===========================================================
# PAGO
# ===========================================================

# GET - Cargar listado de pagos

@app.route("/main3/CargarPagos/<string:entrada>", methods=["GET"])
def api_cargar_pagos(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Pago()
        respuesta["Pagos"] = servicio.CargarPagos()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# POST - Insertar pago
@app.route("/main3/InsertarPago", methods=["POST"])
def api_insertar_pago():

    datos = flask.request.json
    servicio = Servicio_Pago()
    mensaje = servicio.InsertarPago(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar pago
@app.route("/main3/ActualizarPago", methods=["PUT"])
def api_actualizar_pago():

    datos = flask.request.json
    servicio = Servicio_Pago()
    mensaje = servicio.ActualizarPago(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar pago
@app.route("/main3/EliminarPago/<int:id_pago>", methods=["DELETE"])
def api_eliminar_pago(id_pago: int):

    servicio = Servicio_Pago()
    mensaje = servicio.EliminarPago(id_pago)

    return flask.jsonify({"Respuesta": mensaje})

# ===========================================================
# FACTURA
# ===========================================================

# GET - Cargar lista de facturas

@app.route("/main3/CargarFacturas/<string:entrada>", methods=["GET"])
def api_cargar_facturas(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Factura()
        respuesta["Facturas"] = servicio.CargarFacturas()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# POST - Insertar factura
@app.route("/main3/InsertarFactura", methods=["POST"])
def api_insertar_factura():

    datos = flask.request.json
    servicio = Servicio_Factura()
    mensaje = servicio.InsertarFactura(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar factura
@app.route("/main3/ActualizarFactura", methods=["PUT"])
def api_actualizar_factura():

    datos = flask.request.json
    servicio = Servicio_Factura()
    mensaje = servicio.ActualizarFactura(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar factura
@app.route("/main3/EliminarFactura/<int:id_factura>", methods=["DELETE"])
def api_eliminar_factura(id_factura: int):

    servicio = Servicio_Factura()
    mensaje = servicio.EliminarFactura(id_factura)

    return flask.jsonify({"Respuesta": mensaje})



# ===========================================================
# GASTO
# ===========================================================

# GET - Cargar lista de gastos
@app.route("/main3/CargarGastos/<string:entrada>", methods=["GET"])
def api_cargar_gastos(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Gasto()
        respuesta["Gastos"] = servicio.CargarGastos()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# POST - Insertar gasto
@app.route("/main3/InsertarGasto", methods=["POST"])
def api_insertar_gasto():

    datos = flask.request.json
    servicio = Servicio_Gasto()
    mensaje = servicio.InsertarGasto(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar gasto
@app.route("/main3/ActualizarGasto", methods=["PUT"])
def api_actualizar_gasto():

    datos = flask.request.json
    servicio = Servicio_Gasto()
    mensaje = servicio.ActualizarGasto(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar gasto
@app.route("/main3/EliminarGasto/<int:id_gasto>", methods=["DELETE"])
def api_eliminar_gasto(id_gasto: int):

    servicio = Servicio_Gasto()
    mensaje = servicio.EliminarGasto(id_gasto)

    return flask.jsonify({"Respuesta": mensaje})

# ===========================================================
# MULTA
# ===========================================================

# GET - Cargar lista de multas
@app.route("/main3/CargarMultas/<string:entrada>", methods=["GET"])
def api_cargar_multas(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Multa()
        respuesta["Multas"] = servicio.CargarMultas()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# POST - Insertar multas
@app.route("/main3/InsertarMulta", methods=["POST"])
def api_insertar_multa():

    datos = flask.request.json
    servicio = Servicio_Multa()
    mensaje = servicio.InsertarMulta(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar multa
@app.route("/main3/ActualizarMulta", methods=["PUT"])
def api_actualizar_multa():

    datos = flask.request.json
    servicio = Servicio_Multa()
    mensaje = servicio.ActualizarMulta(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar multa
@app.route("/main3/EliminarMulta/<int:id_multa>", methods=["DELETE"])
def api_eliminar_multa(id_multa: int):

    servicio = Servicio_Multa()
    mensaje = servicio.EliminarMulta(id_multa)

    return flask.jsonify({"Respuesta": mensaje})


# ===========================================================
#  INCIDENTE
# ===========================================================

# GET - Cargar lista de incidentes
@app.route("/main3/CargarIncidentes/<string:entrada>", methods=["GET"])
def api_cargar_incidentes(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Incidente()
        respuesta["Incidentes"] = servicio.CargarIncidentes()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# POST - Insertar incidente
@app.route("/main3/InsertarIncidente", methods=["POST"])
def api_insertar_incidente():

    datos = flask.request.json
    servicio = Servicio_Incidente()
    mensaje = servicio.InsertarIncidente(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar incidente
@app.route("/main3/ActualizarIncidente", methods=["PUT"])
def api_actualizar_incidente():

    datos = flask.request.json
    servicio = Servicio_Incidente()
    mensaje = servicio.ActualizarIncidente(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar incidente
@app.route("/main3/EliminarIncidente/<int:id_incidente>", methods=["DELETE"])
def api_eliminar_incidente(id_incidente: int):

    servicio = Servicio_Incidente()
    mensaje = servicio.EliminarIncidente(id_incidente)

    return flask.jsonify({"Respuesta": mensaje})

# ===========================================================
#  MEMBRESIA
# ===========================================================

# GET - Cargar lista de membresias
@app.route("/main3/CargarMembresias/<string:entrada>", methods=["GET"])
def api_cargar_membresias(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Membresia()
        respuesta["Membresias"] = servicio.CargarMembresias()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# POST - Insertar membresia
@app.route("/main3/InsertarMembresia", methods=["POST"])
def api_insertar_membresia():

    datos = flask.request.json
    servicio = Servicio_Membresia()
    mensaje = servicio.InsertarMembresia(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar membresia
@app.route("/main3/ActualizarMembresia", methods=["PUT"])
def api_actualizar_membresia():

    datos = flask.request.json
    servicio = Servicio_Membresia()
    mensaje = servicio.ActualizarMembresia(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar membresia
@app.route("/main3/EliminarMembresia/<int:id_membresia>", methods=["DELETE"])
def api_eliminar_membresia(id_membresia: int):

    servicio = Servicio_Membresia()
    mensaje = servicio.EliminarMembresia(id_membresia)

    return flask.jsonify({"Respuesta": mensaje})


# ===========================================================
# PROMOCION
# ===========================================================

# GET - Cargar lista de promociones
@app.route("/main3/CargarPromociones/<string:entrada>", methods=["GET"])
def api_cargar_promociones(entrada: str):

    respuesta = {}
    try:
        entrada = entrada.replace("'", '"')
        datos = json.loads(entrada)

        servicio = Servicio_Promocion()
        respuesta["Promociones"] = servicio.CargarPromociones()
        respuesta["Respuesta"] = "OK"
        respuesta["Entrada"] = datos

        return flask.jsonify(respuesta)

    except Exception as ex:
        respuesta["Respuesta"] = "Error"
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta)

# POST - Insertar promoción
@app.route("/main3/InsertarPromocion", methods=["POST"])
def api_insertar_promocion():

    datos = flask.request.json
    servicio = Servicio_Promocion()
    mensaje = servicio.InsertarPromocion(datos)

    return flask.jsonify({"Respuesta": mensaje})

# PUT - Actualizar promocion
@app.route("/main3/ActualizarPromocion", methods=["PUT"])
def api_actualizar_promocion():

    datos = flask.request.json
    servicio = Servicio_Promocion()
    mensaje = servicio.ActualizarPromocion(datos)

    return flask.jsonify({"Respuesta": mensaje})

# DELETE - Eliminar promocion
@app.route("/main3/EliminarPromocion/<int:id_promocion>", methods=["DELETE"])
def api_eliminar_promocion(id_promocion: int):

    servicio = Servicio_Promocion()
    mensaje = servicio.EliminarPromocion(id_promocion)

    return flask.jsonify({"Respuesta": mensaje})


app.run("localhost", 4040)

