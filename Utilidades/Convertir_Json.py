# Utilidades/convertir_json.py


# Utilidades/Convertir_Json.py

def clientes_to_json(lista):
    resultado = []
    for c in lista:
        resultado.append({
            "IdCliente": c.GetIdCliente(),
            "Nombre": c.GetNombre(),
            "Documento": c.GetDocumento(),
            "Telefono": c.GetTelefono(),
            "Correo": c.GetCorreo(),
            "Direccion": c.GetDireccion()
        })
    return resultado


def vehiculos_to_json(lista):
    resultado = []
    for v in lista:
        resultado.append({
            "IdVehiculo": v.GetIdVehiculo(),
            "Placa": v.GetPlaca(),
            "Marca": v.GetMarca(),
            "Color": v.GetColor(),
            "IdTipo": v.GetIdTipo(),
            "IdCliente": v.GetIdCliente()
        })
    return resultado

def empleados_to_json(lista):
    resultado = []
    for e in lista:
        resultado.append({
            "IdEmpleado": e.GetIdEmpleado(),
            "Nombre": e.GetNombre(),
            "Documento": e.GetDocumento(),
            "Telefono": e.GetTelefono(),
            "Correo": e.GetCorreo(),
            "IdRol": e.GetIdRol()
        })
    return resultado

def roles_to_json(lista: list) -> dict:
    respuesta = {}
    contador = 0

    for rol in lista:
        temp = {
            "IdRol": rol.GetIdRol(),
            "Nombre": rol.GetNombre(),
            "Descripcion": rol.GetDescripcion()
        }
        respuesta[str(contador)] = temp
        contador += 1

    return respuesta

def tiposvehiculo_to_json(lista):
    resultado = []
    for t in lista:
        resultado.append({
            "IdTipo": t.GetIdTipo(),
            "Nombre": t.GetNombre(),
            "Descripcion": t.GetDescripcion()
        })
    return resultado

def tarifas_to_json(lista):
    resultado = []
    for t in lista:
        resultado.append({
            "IdTarifa": t.GetIdTarifa(),
            "IdTipo": t.GetIdTipo(),
            "TipoTarifa": t.GetTipoTarifa(),
            "Valor": t.GetValor()
        })
    return resultado

def entradasalida_to_json(lista):
    resultado = []
    for r in lista:
        resultado.append({
            "IdRegistro": r.GetIdRegistro(),
            "IdVehiculo": r.GetIdVehiculo(),
            "IdEmpleado": r.GetIdEmpleado(),
            "FechaEntrada": r.GetFechaEntrada(),
            "FechaSalida": r.GetFechaSalida(),
            "Espacio": r.GetEspacio()
        })
    return resultado

def metodos_to_json(lista):
    resultado = []
    for m in lista:
        resultado.append({
            "IdMetodo": m.GetIdMetodo(),
            "Nombre": m.GetNombre(),
            "Descripcion": m.GetDescripcion()
        })
    return resultado

def pagos_to_json(lista):
    resultado = []
    for p in lista:
        resultado.append({
            "IdPago": p.GetIdPago(),
            "IdRegistro": p.GetIdRegistro(),
            "IdMetodo": p.GetIdMetodo(),
            "Monto": p.GetMonto(),
            "FechaPago": p.GetFechaPago(),
            "IdEmpleado": p.GetIdEmpleado()
        })
    return resultado

def facturas_to_json(lista):
    resultado = []
    for f in lista:
        resultado.append({
            "IdFactura": f.GetIdFactura(),
            "IdPago": f.GetIdPago(),
            "NumeroFactura": f.GetNumeroFactura(),
            "FechaEmision": f.GetFechaEmision(),
            "Total": f.GetTotal()
        })
    return resultado

def gastos_to_json(lista):
    resultado = []
    for g in lista:
        resultado.append({
            "IdGasto": g.GetIdGasto(),
            "Descripcion": g.GetDescripcion(),
            "Monto": g.GetMonto(),
            "Fecha": g.GetFecha(),
            "IdEmpleado": g.GetIdEmpleado()
        })
    return resultado

def multas_to_json(lista):
    resultado = []
    for m in lista:
        resultado.append({
            "IdMulta": m.GetIdMulta(),
            "IdRegistro": m.GetIdRegistro(),
            "Motivo": m.GetMotivo(),
            "Valor": m.GetValor(),
            "Fecha": m.GetFecha()
        })
    return resultado

def incidentes_to_json(lista):
    resultado = []
    for i in lista:
        resultado.append({
            "IdIncidente": i.GetIdIncidente(),
            "IdRegistro": i.GetIdRegistro(),
            "Descripcion": i.GetDescripcion(),
            "Fecha": i.GetFecha(),
            "IdEmpleado": i.GetIdEmpleado()
        })
    return resultado

def membresias_to_json(lista):
    resultado = []
    for m in lista:
        resultado.append({
            "IdMembresia": m.GetIdMembresia(),
            "IdCliente": m.GetIdCliente(),
            "FechaInicio": m.GetFechaInicio(),
            "FechaFin": m.GetFechaFin(),
            "Tipo": m.GetTipo(),
            "Descuento": m.GetDescuento(),
            "Estado": m.GetEstado()
        })
    return resultado

def promociones_to_json(lista):
    resultado = []
    for p in lista:
        resultado.append({
            "IdPromocion": p.GetIdPromocion(),
            "Nombre": p.GetNombre(),
            "Descripcion": p.GetDescripcion(),
            "Descuento": p.GetDescuento(),
            "FechaInicio": p.GetFechaInicio(),
            "FechaFin": p.GetFechaFin()
        })
    return resultado

