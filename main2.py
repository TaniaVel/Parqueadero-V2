from Repositorios.Cone_Cliente import Conexion_Cliente
from Entidades.Cliente import Cliente

from Repositorios.Cone_TipoVehiculo import Conexion_TipoVehiculo
from Entidades.TipoVehiculo import TipoVehiculo

from Repositorios.Cone_Vehiculo import Conexion_Vehiculo
from Entidades.Vehiculo import Vehiculo

from Repositorios.Cone_Registro import Conexion_Registro
from Entidades.Entradasalida import Entradasalida
from datetime import datetime

from Repositorios.Cone_RolEmpleado import Conexion_RolEmpleado
from Entidades.RolEmpleado import RolEmpleado

from Entidades.Empleado import Empleado
from Repositorios.Conexion_Empleado import Conexion_Empleado

from Repositorios.Cone_MetodoPago import Conexion_MetodoPago
from Entidades.MetodoPago import MetodoPago

from Repositorios.Cone_Tarifa import Conexion_Tarifa
from Entidades.Tarifa import Tarifa

from Repositorios.Cone_Incidente import Conexion_Incidente
from Entidades.Incidente import Incidente

from Repositorios.Cone_Pago import Conexion_Pago
from Entidades.Pago import Pago

from Repositorios.Cone_Promocion import Conexion_Promocion
from Entidades.Promocion import Promocion

from Repositorios.Cone_Membresia import Conexion_Membresia
from Entidades.Membresia import Membresia


from Repositorios.Cone_Factura import Conexion_Factura
from Entidades.Factura import Factura


from Repositorios.Cone_Gasto import Conexion_Gasto
from Entidades.Gasto import Gasto

from Repositorios.Cone_Multa import Conexion_Multa
from Entidades.Multa import Multa
# ================================
# Funciones para cada Clase
# ================================

 
#  ************ CLIENTE 
def gestionar_cliente():
    gestion_cliente = Conexion_Cliente()
# -------------------- Insertar cliente --------------------
    print("\n--- Insertar Cliente ---")
    c = Cliente()
    c.SetNombre("Sara Vélez")
    c.SetDocumento("987654321")
    c.SetTelefono("3111234567")
    c.SetCorreo("sara@gmail.com")
    c.SetDireccion("Calle 45 #12-34")
    gestion_cliente.InsertarCliente(c)

    print("\n--- Listar Clientes ---")
    clientes = gestion_cliente.CargarClientes()
    for cl in clientes:
        print(f"{cl.GetIdCliente()} - {cl.GetNombre()} - {cl.GetDocumento()}")

# -------------------- Actualizar cliente --------------------

    print("\n--- Actualizar Cliente ---")
    c_actualizar = Cliente()
    c_actualizar.SetIdCliente(34)
    c_actualizar.SetNombre("Sara Vélez C")
    c_actualizar.SetTelefono("30000002")
    c_actualizar.SetCorreo("sara.nuevo@gmail.com")
    c_actualizar.SetDireccion("Calle 45 #12-34")
    c_actualizar.SetDocumento("987654321")
    gestion_cliente.ActualizarCliente(c_actualizar)

# -------------------- Listar después de actualiazaR --------------------
    print("\nClientes después de actualizar:")
    clientes = gestion_cliente.CargarClientes()
    for cl in clientes:
        print(f"{cl.GetIdCliente()} - {cl.GetNombre()} - {cl.GetDocumento()} - {cl.GetTelefono()} - {cl.GetCorreo()}")

# -------------------- Eliminar Cliente --------------------
    print("\n--- Eliminar Cliente ---")
    gestion_cliente.EliminarCliente(21)


#  ************ TIPO VEHICULO
def gestionar_tipo_vehiculo():
    gestion_tipo = Conexion_TipoVehiculo()

# -------------------- Insertar tipo Vehículo --------------------
    print("\n--- Insertar Tipo de Vehículo ---")
    t = TipoVehiculo()
    t.SetNombre("Motocicleta")
    t.SetDescripcion("Vehículo de dos ruedas")
    gestion_tipo.InsertarTipoVehiculo(t)

    print("\n--- Listar Tipos de Vehículo ---")
    tipos = gestion_tipo.CargarTipoVehiculos()
    for tp in tipos:
        print(f"{tp.GetIdTipo()} - {tp.GetNombre()} - {tp.GetDescripcion()}")

# -------------------- Actualizar tipo vehiculo--------------------
    print("\n--- Actualizar Tipo de Vehículo ---")
    t_actualizar = TipoVehiculo()
    t_actualizar.SetIdTipo(1)
    t_actualizar.SetNombre("Motocicleta Eléctrica")
    t_actualizar.SetDescripcion("Vehículo de dos ruedas con motor eléctrico")
    gestion_tipo.ActualizarTipoVehiculo(t_actualizar)

# -------------------- Listar después de actualiazaR --------------------
    print("\nTipos de vehículos después de actualizar:")
    tipos = gestion_tipo.CargarTipoVehiculos()
    for tp in tipos:
        print(f"{tp.GetIdTipo()} - {tp.GetNombre()} - {tp.GetDescripcion()}")

# -------------------- Eliminar vehiçulo--------------------
    print("\n--- Eliminar Tipo de Vehículo ---")
    gestion_tipo.EliminarTipoVehiculo(2)


#  ************  VEHICULO

def gestionar_vehiculo():
    gestion_vehiculo = Conexion_Vehiculo()
# -------------------- Insertar  Vehículo --------------------
    print("\n--- Insertar Vehículo ---")
    v = Vehiculo()
    v.SetPlaca("XYZ123")
    v.SetMarca("Yamaha")
    v.SetColor("Rojo")
    v.SetIdTipo(1)
    v.SetIdCliente(34)
    gestion_vehiculo.InsertarVehiculo(v)

    print("\n--- Listar Vehículos ---")
    vehiculos = gestion_vehiculo.CargarVehiculos()
    for vh in vehiculos:
        print(f"{vh.GetIdVehiculo()} - {vh.GetPlaca()} - {vh.GetMarca()} - {vh.GetColor()} - "
              f"Tipo: {vh.GetIdTipo()} - Cliente: {vh.GetIdCliente()}")

# -------------------- Actualizar vehiculo--------------------

    print("\n--- Actualizar Vehículo ---")
    v_actualizar = Vehiculo()
    v_actualizar.SetIdVehiculo(1)
    v_actualizar.SetPlaca("XYZ123")
    v_actualizar.SetMarca("Honda")
    v_actualizar.SetColor("Negro")
    v_actualizar.SetIdTipo(1)
    v_actualizar.SetIdCliente(34)
    gestion_vehiculo.ActualizarVehiculo(v_actualizar)

# -------------------- Listar después de actualiazaR --------------------

    vehiculos = gestion_vehiculo.CargarVehiculos()
    for vh in vehiculos:
        print(f"{vh.GetIdVehiculo()} - {vh.GetPlaca()} - {vh.GetMarca()} - {vh.GetColor()} - "
              f"Tipo: {vh.GetIdTipo()} - Cliente: {vh.GetIdCliente()}")
        
# -------------------- Eliminar vehiçulo--------------------

    print("\n--- Eliminar Vehículo ---")
    gestion_vehiculo.EliminarVehiculo(2)

#  ************ REGISTRO (ENTRADA Y SALIDA)

def gestionar_registro():
    gestion_registro = Conexion_Registro()
# -------------------- Insertar  registro --------------------
    print("\n--- Insertar Registro de Entrada ---")
    r = Entradasalida()
    r.SetIdVehiculo(3)  # debe existir
    r.SetIdEmpleado(3)  # debe existir
    r.SetFechaEntrada(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    r.SetEspacio("A12")
    gestion_registro.InsertarRegistro(r)

    print("\n--- Listar Registros ---")
    registros = gestion_registro.CargarRegistros()
    for rg in registros:
        print(f"{rg.GetIdRegistro()} - Vehículo: {rg.GetIdVehiculo()} - Empleado: {rg.GetIdEmpleado()} - "
              f"Entrada: {rg.GetFechaEntrada()} - Salida: {rg.GetFechaSalida()} - Espacio: {rg.GetEspacio()}")

# -------------------- Actualizar  registro --------------------

    print("\n--- Actualizar Registro (Salida) ---")
    r_actualizar = Entradasalida()
    r_actualizar.SetIdRegistro(5)  # debe existir
    r_actualizar.SetFechaSalida(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    gestion_registro.ActualizarSalida(r_actualizar)

# -------------------- Eliminar  registro --------------------
    print("\n--- Eliminar Registro ---")
    gestion_registro.EliminarRegistro(3) # debe existir

#  ************ ROL EMPLEADO

def gestionar_rol_empleado():
    gestion_rol = Conexion_RolEmpleado()

# -------------------- Insertar rol empleado  --------------------

    print("\n--- Insertar Rol de Empleado ---")
    r = RolEmpleado()
    r.SetNombre("Valet Parking2")  # debe ser diferente a uno que este en la bd
    r.SetDescripcion("Encargado de ayudar con el parqueo")
    gestion_rol.InsertarRol(r)

    # mstrar roles
    print("\n--- Listar Roles de Empleado ---")
    roles = gestion_rol.CargarRoles()
    for rl in roles:
        print(f"{rl.GetIdRol()} - {rl.GetNombre()} - {rl.GetDescripcion()}")

# -------------------- actualizar rol empleado  --------------------

    print("\n--- Actualizar Rol de Empleado ---")
    r_actualizar = RolEmpleado()
    r_actualizar.SetIdRol(1)  # debe existir
    r_actualizar.SetNombre("Supervisor2") #Vigilante
    r_actualizar.SetDescripcion("Supervisor prueba")  # Responsable de revisión de cámaras
    gestion_rol.ActualizarRol(r_actualizar)

# -------------------- Listar después de actualiazaR  --------------------
    roles = gestion_rol.CargarRoles()
    print("\nRoles después de actualizar:")
    for rl in roles:
        print(f"{rl.GetIdRol()} - {rl.GetNombre()} - {rl.GetDescripcion()}")

# -------------------- Eliminar Rol  --------------------
    print("\n--- Eliminar Rol de Empleado ---")
    gestion_rol.EliminarRol(5)  # debe existir

#  ************ EMPLEADO

def gestionar_empleado():
    gestion_empleado = Conexion_Empleado()
# -------------------- Insertar datos de empleado  --------------------

    print("\n--- Insertar Empleado ---")
    e = Empleado()
    e.SetNombre("Carlos Pérez")
    e.SetDocumento("1020304050")
    e.SetTelefono("3123456789")
    e.SetCorreo("carlos.perez@gmail.com")
    e.SetIdRol(1)  # Asegúrate de que el rol 1 exista
    gestion_empleado.InsertarEmpleado(e)

    print("\n--- Listar Empleados ---")
    empleados = gestion_empleado.CargarEmpleados()
    for emp in empleados:
        print(f"{emp.GetIdEmpleado()} - {emp.GetNombre()} - {emp.GetDocumento()} - {emp.GetTelefono()} - {emp.GetCorreo()} - Rol: {emp.GetIdRol()}")

# -------------------- Actualizar datos de empleado  --------------------

    print("\n--- Actualizar Empleado ---")
    e_actualizar = Empleado()
    e_actualizar.SetIdEmpleado(4)  # debe existir
    e_actualizar.SetNombre("Carlos Pérez")
    e_actualizar.SetTelefono("3100000000")
    e_actualizar.SetCorreo("carlos.actualizado@gmail.com")
    e_actualizar.SetIdRol(1) # debe existir
    gestion_empleado.ActualizarEmpleado(e_actualizar)

# -------------------- Listar después de actualiazaR  --------------------

    print("\nEmpleados después de actualizar:")
    empleados = gestion_empleado.CargarEmpleados()
    for emp in empleados:
        print(f"{emp.GetIdEmpleado()} - {emp.GetNombre()} - {emp.GetTelefono()} - {emp.GetCorreo()} - Rol: {emp.GetIdRol()}")

# --------------------Eliminar empleado  --------------------

    print("\n--- Eliminar Empleado ---")
    gestion_empleado.EliminarEmpleado(5)# debe existir

#  ************ METODO DE PAGO 
def gestionar_metodoPago():
    gestion_metodo = Conexion_MetodoPago()

# --------------------Insertar método de pago  --------------------

    print("\n--- Insertar Método de Pago ---")
    m = MetodoPago()
    m.SetNombre("Tarjeta Débito")
    m.SetDescripcion("Pago con tarjeta débito")
    gestion_metodo.InsertarMetodo(m)

    print("\n--- Listar Métodos de Pago ---")
    metodos = gestion_metodo.CargarMetodos()
    for mp in metodos:
        print(f"{mp.GetIdMetodo()} - {mp.GetNombre()} - {mp.GetDescripcion()}")

# --------------------Actualizar método de pago  --------------------

    print("\n--- Actualizar Método de Pago ---")
    m_actualizar = MetodoPago()
    m_actualizar.SetIdMetodo(2)  #debe existir
    m_actualizar.SetNombre("Tarjeta débito ss ")
    m_actualizar.SetDescripcion("Pago con tarjeta de débito ss")
    gestion_metodo.ActualizarMetodo(m_actualizar)

# --------------------Listar después de actualiazaR  --------------------

    print("\nMétodos de Pago después de actualizar:")
    metodos = gestion_metodo.CargarMetodos()
    for mp in metodos:
        print(f"{mp.GetIdMetodo()} - {mp.GetNombre()} - {mp.GetDescripcion()}")

# --------------------Eliminar método de pago  --------------------

    print("\n--- Eliminar Método de Pago ---")
    gestion_metodo.EliminarMetodo(3) #debe existir

#  ************ PAGO
def gestionar_pago():

    gestion_pago = Conexion_Pago()

# --------------------Insertar pago --------------------

    print("\n--- Insertar Pago ---")
    p = Pago()
    p.SetIdRegistro(5)  #debe existir
    p.SetIdMetodo(1)    #debe existir
    p.SetMonto(15000.00)
    p.SetFechaPago(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    p.SetIdEmpleado(3)  #debe existir
    gestion_pago.InsertarPago(p)

    print("\n--- Listar Pagos ---")
    pagos = gestion_pago.CargarPagos()
    for pg in pagos:
        print(f"{pg.GetIdPago()} - Registro: {pg.GetIdRegistro()} - Método: {pg.GetIdMetodo()} - "
              f"Monto: {pg.GetMonto()} - Fecha: {pg.GetFechaPago()} - Empleado: {pg.GetIdEmpleado()}")

# --------------------Actualizar pago --------------------

    print("\n--- Actualizar Pago ---")
    p_actualizar = Pago()
    p_actualizar.SetIdPago(1)  #debe existir
    p_actualizar.SetIdRegistro(1) #debe existir
    p_actualizar.SetIdMetodo(1)#debe existir
    p_actualizar.SetMonto(20000.00)
    p_actualizar.SetFechaPago(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    p_actualizar.SetIdEmpleado(1) #debe existir
    gestion_pago.ActualizarPago(p_actualizar)

# -------------------- Listar después de actualiazaR  --------------------

    print("\nPagos después de actualizar:")
    pagos = gestion_pago.CargarPagos()
    for pg in pagos:
        print(f"{pg.GetIdPago()} - Registro: {pg.GetIdRegistro()} - Método: {pg.GetIdMetodo()} - "
              f"Monto: {pg.GetMonto()} - Fecha: {pg.GetFechaPago()} - Empleado: {pg.GetIdEmpleado()}")

# -------------------- Eliminar --------------------

    print("\n--- Eliminar Pago ---")
    gestion_pago.EliminarPago(2)  #debe existir

#  ************ TARIFA
def gestionar_tarifa():
    gestion_tarifa = Conexion_Tarifa()
# -------------------- Insertar tarifa --------------------

    print("\n--- Insertar Tarifa ---")
    t = Tarifa()
    t.SetIdTipo(1)  #debe existir
    t.SetTipoTarifa("Hora")  # Puede ser 'Hora', 'Dia' o 'Mes'
    t.SetValor(5000.00)
    gestion_tarifa.InsertarTarifa(t)

    print("\n--- Listar Tarifas ---")
    tarifas = gestion_tarifa.CargarTarifas()
    for tr in tarifas:
        print(f"{tr.GetIdTarifa()} - Tipo Vehículo: {tr.GetIdTipo()} - Tipo Tarifa: {tr.GetTipoTarifa()} - Valor: {tr.GetValor()}")

# -------------------- actualizar datos de tarifa --------------------

    print("\n--- Actualizar Tarifa ---")
    t_actualizar = Tarifa()
    t_actualizar.SetIdTarifa(1)  #debe existir
    t_actualizar.SetIdTipo(2)     #debe existir
    t_actualizar.SetTipoTarifa("Dia")
    t_actualizar.SetValor(30000.00)
    gestion_tarifa.ActualizarTarifa(t_actualizar)

# -------------------- Listar después de actualiazaR  --------------------

    print("\nTarifas después de actualizar:")
    tarifas = gestion_tarifa.CargarTarifas()
    for tr in tarifas:
        print(f"{tr.GetIdTarifa()} - Tipo Vehículo: {tr.GetIdTipo()} - Tipo Tarifa: {tr.GetTipoTarifa()} - Valor: {tr.GetValor()}")

# -------------------- eliminar datos de tarifa --------------------

    print("\n--- Eliminar Tarifa ---")
    gestion_tarifa.EliminarTarifa(2)  #debe existir

#  ************ EMPLEADO
def gestionar_incidente():

    gestion_incidente = Conexion_Incidente()

# -------------------- Insertar Incidente --------------------
    print("\n--- Insertar Incidente ---")
    inc = Incidente()
    inc.SetIdRegistro(5)   #debe existir
    inc.SetDescripcion("Choque leve en estacionamiento")
    inc.SetFecha(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    inc.SetIdEmpleado(3)  #  #debe existir - Opcional, si se registra quién reporta
    gestion_incidente.InsertarIncidente(inc)

# -------------------- Listar Incidentes --------------------
    print("\n--- Listar Incidentes ---")
    incidentes = gestion_incidente.CargarIncidentes()
    for i in incidentes:
        print(f"{i.GetIdIncidente()} - Registro: {i.GetIdRegistro()} - Descripción: {i.GetDescripcion()} - "
              f"Fecha: {i.GetFecha()} - Empleado: {i.GetIdEmpleado()}")

# -------------------- Actualizar Incidente --------------------
    print("\n--- Actualizar Incidente ---")
    inc_actualizar = Incidente()
    inc_actualizar.SetIdIncidente(2)   #debe existir
    inc_actualizar.SetIdRegistro(1) #debe existir
    inc_actualizar.SetDescripcion("Choque leve, sin daños mayores")
    inc_actualizar.SetFecha(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    inc_actualizar.SetIdEmpleado(1)  #debe existir
    gestion_incidente.ActualizarIncidente(inc_actualizar)

# -------------------- Eliminar Incidente --------------------
    print("\n--- Eliminar Incidente ---")
    gestion_incidente.EliminarIncidente(3)   #debe existir

#  ************ PROMOCION
def gestionar_promocion():

    gestion_promocion = Conexion_Promocion()

# -------------------- Insertar Promoción --------------------
    print("\n--- Insertar Promoción ---")
    p = Promocion()
    p.SetNombre("Descuento Primavera")
    p.SetDescripcion("20% de descuento en el mes de septiembre")
    p.SetDescuento(20.0)
    p.SetFechaInicio("2025-09-01")
    p.SetFechaFin("2025-09-30")
    gestion_promocion.InsertarPromocion(p)

# -------------------- Listar Promociones --------------------
    print("\n--- Listar Promociones ---")
    promociones = gestion_promocion.CargarPromociones()
    for pr in promociones:
        print(f"{pr.GetIdPromocion()} - {pr.GetNombre()} - {pr.GetDescripcion()} - "
              f"Descuento: {pr.GetDescuento()}% - Inicio: {pr.GetFechaInicio()} - Fin: {pr.GetFechaFin()}")

# -------------------- Actualizar Promoción --------------------
    print("\n--- Actualizar Promoción ---")
    p_actualizar = Promocion()
    p_actualizar.SetIdPromocion(1)  #debe existir
    p_actualizar.SetNombre("Descuento Otoño")
    p_actualizar.SetDescripcion("15% de descuento en el mes de octubre")
    p_actualizar.SetDescuento(15.0)
    p_actualizar.SetFechaInicio("2025-10-01")
    p_actualizar.SetFechaFin("2025-10-31")
    gestion_promocion.ActualizarPromocion(p_actualizar)

# -------------------- Listar después de actualizar --------------------
    print("\nPromociones después de actualizar:")
    promociones = gestion_promocion.CargarPromociones()
    for pr in promociones:
        print(f"{pr.GetIdPromocion()} - {pr.GetNombre()} - {pr.GetDescripcion()} - "
              f"Descuento: {pr.GetDescuento()}% - Inicio: {pr.GetFechaInicio()} - Fin: {pr.GetFechaFin()}")

# -------------------- Eliminar Promoción --------------------
    print("\n--- Eliminar Promoción ---")
    gestion_promocion.EliminarPromocion(2)  #debe existir

#  ************ MEMBRESIA

def gestionar_membresia():

    gestion_membresia = Conexion_Membresia()

# -------------------- Insertar Membresia --------------------

    print("\n--- Insertar Membresía ---")
    m = Membresia()
    m.SetIdCliente(34)  #debe existir
    m.SetFechaInicio("2025-10-01")
    m.SetFechaFin("2025-12-31")
    m.SetTipo("Trimestral")
    m.SetDescuento(10.0)
    m.SetEstado("Activa")
    gestion_membresia.InsertarMembresia(m)

    print("\n--- Listar Membresías ---")
    membresias = gestion_membresia.CargarMembresias()
    for mb in membresias:
        print(f"{mb.GetIdMembresia()} - Cliente: {mb.GetIdCliente()} - Tipo: {mb.GetTipo()} - "
              f"Inicio: {mb.GetFechaInicio()} - Fin: {mb.GetFechaFin()} - Descuento: {mb.GetDescuento()}% - Estado: {mb.GetEstado()}")

# -------------------- Actualizar Membresia --------------------

    print("\n--- Actualizar Membresía ---")
    m_actualizar = Membresia()
    m_actualizar.SetIdMembresia(1)  #debe existir
    m_actualizar.SetIdCliente(34) #debe existir
    m_actualizar.SetFechaInicio("2025-10-01")
    m_actualizar.SetFechaFin("2025-12-31")
    m_actualizar.SetTipo("Trimestral")
    m_actualizar.SetDescuento(15.0)
    m_actualizar.SetEstado("Activa")
    gestion_membresia.ActualizarMembresia(m_actualizar)

# -------------------- Listar después de actualizar --------------------

    print("\nMembresías después de actualizar:")
    membresias = gestion_membresia.CargarMembresias()
    for mb in membresias:
        print(f"{mb.GetIdMembresia()} - Cliente: {mb.GetIdCliente()} - Tipo: {mb.GetTipo()} - "
              f"Inicio: {mb.GetFechaInicio()} - Fin: {mb.GetFechaFin()} - Descuento: {mb.GetDescuento()}% - Estado: {mb.GetEstado()}")

# -------------------- Eliminar membresia --------------------

    print("\n--- Eliminar Membresía ---")
    gestion_membresia.EliminarMembresia(2)  #debe existir

#  ************ MULTA

def gestionar_multa():

    gestion_multa = Conexion_Multa()
# -------------------- Insertar multa --------------------

    print("\n--- Insertar Multa ---")
    m = Multa()
    m.SetIdRegistro(6)   #debe existir
    m.SetMotivo("Exceso de tiempo")
    m.SetValor(5000.00)
    m.SetFecha(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    gestion_multa.InsertarMulta(m)

    print("\n--- Listar Multas ---")
    multas = gestion_multa.CargarMultas()
    for mu in multas:
        print(f"{mu.GetIdMulta()} - Registro: {mu.GetIdRegistro()} - Motivo: {mu.GetMotivo()} - "
              f"Valor: {mu.GetValor()} - Fecha: {mu.GetFecha()}")

# -------------------- Actualizar multa --------------------

    print("\n--- Actualizar Multa ---")
    m_actualizar = Multa()
    m_actualizar.SetIdMulta(1)  #debe existir
    m_actualizar.SetIdRegistro(5)
    m_actualizar.SetMotivo("Pérdida de tiquete")
    m_actualizar.SetValor(15000.00)
    m_actualizar.SetFecha(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    gestion_multa.ActualizarMulta(m_actualizar)

# -------------------- Listar después de actualizar --------------------

    print("\nMultas después de actualizar:")
    multas = gestion_multa.CargarMultas()
    for mu in multas:
        print(f"{mu.GetIdMulta()} - Registro: {mu.GetIdRegistro()} - Motivo: {mu.GetMotivo()} - "
              f"Valor: {mu.GetValor()} - Fecha: {mu.GetFecha()}")

# --------------------eliminar multa --------------------

    print("\n--- Eliminar Multa ---")
    gestion_multa.EliminarMulta(3)  #debe existir

#  ************ FACTURA
def gestionar_factura():
    gestion_factura = Conexion_Factura()
# --------------------Insertar Factura --------------------

    print("\n--- Insertar Factura ---")
    f = Factura()
    f.SetIdPago(1)  #debe existir
    f.SetNumeroFactura("FAC-001")
    f.SetFechaEmision(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    f.SetTotal(15000.00)
    gestion_factura.InsertarFactura(f)

    print("\n--- Listar Facturas ---")
    facturas = gestion_factura.CargarFacturas()
    for fc in facturas:
        print(f"{fc.GetIdFactura()} - Pago: {fc.GetIdPago()} - Número: {fc.GetNumeroFactura()} - Fecha: {fc.GetFechaEmision()} - Total: {fc.GetTotal()}")

# --------------------actualizar factura --------------------

    print("\n--- Actualizar Factura ---")
    f_actualizar = Factura()
    f_actualizar.SetIdFactura(1)  #debe existir
    f_actualizar.SetIdPago(1) #debe existir
    f_actualizar.SetNumeroFactura("FAC-001-EDIT")
    f_actualizar.SetFechaEmision(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    f_actualizar.SetTotal(20000.00)
    gestion_factura.ActualizarFactura(f_actualizar)

# -------------------- Listar después de actualizar --------------------

    print("\nFacturas después de actualizar:")
    facturas = gestion_factura.CargarFacturas()
    for fc in facturas:
        print(f"{fc.GetIdFactura()} - Pago: {fc.GetIdPago()} - Número: {fc.GetNumeroFactura()} - Fecha: {fc.GetFechaEmision()} - Total: {fc.GetTotal()}")

# -------------------- Eliminar factura --------------------

    print("\n--- Eliminar Factura ---")
    gestion_factura.EliminarFactura(2)  #debe existir

#  ************ GASTO
def gestionar_gasto():
    gestion_gasto = Conexion_Gasto()
# -------------------- Insertar Gasto --------------------

    print("\n--- Insertar Gasto ---")
    g = Gasto()
    g.SetDescripcion("Compra de insumos")
    g.SetMonto(50000.00)
    g.SetFecha(datetime.now().strftime("%Y-%m-%d"))
    g.SetIdEmpleado(1)  #debe existir
    gestion_gasto.InsertarGasto(g)

    print("\n--- Listar Gastos ---")
    gastos = gestion_gasto.CargarGastos()
    for gt in gastos:
        print(f"{gt.GetIdGasto()} - {gt.GetDescripcion()} - Monto: {gt.GetMonto()} - Fecha: {gt.GetFecha()} - Empleado: {gt.GetIdEmpleado()}")

# -------------------- actualizar  Gasto --------------------

    print("\n--- Actualizar Gasto ---")
    g_actualizar = Gasto()
    g_actualizar.SetIdGasto(1)  # ID existente
    g_actualizar.SetDescripcion("Compra de insumos y materiales")
    g_actualizar.SetMonto(60000.00)
    g_actualizar.SetFecha(datetime.now().strftime("%Y-%m-%d"))
    g_actualizar.SetIdEmpleado(1)
    gestion_gasto.ActualizarGasto(g_actualizar)

# -------------------- Listar después de actualizar--------------------

    print("\n--- Gastos después de actualizar ---")
    gastos = gestion_gasto.CargarGastos()
    for gt in gastos:
        print(f"{gt.GetIdGasto()} - {gt.GetDescripcion()} - Monto: {gt.GetMonto()} - Fecha: {gt.GetFecha()} - Empleado: {gt.GetIdEmpleado()}")

# -------------------- Eliminar--------------------

    print("\n--- Eliminar Gasto ---")
    gestion_gasto.EliminarGasto(2) #debe existir


# ================================
# Menú principal
# ================================
if __name__ == "__main__":
    while True:
        print("\n==========================")
        print("   MENÚ DE GESTIÓN")
        print("==========================")
        print("1. Gestionar Cliente")
        print("2. Gestionar Tipo de Vehículo")
        print("3. Gestionar Vehículo")
        print("4. Gestionar Registro de Entrada/Salida")
        print("5. Gestionar Rol de Empleado")
        print("6. Gestionar Empleado")
        print("7. Gestionar Método de Pago")
        print("8. Gestionar Pago")
        print("9. Gestionar Tarifa")
        print("10. Gestionar Incidentes")
        print("11. Gestionar Promociones")
        print("12. Gestionar membresias")
        print("13. Gestionar Multas")
        print("14. Gestionar Factura")
        print("15. Gestionar Gastos")
        print("16. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_cliente()
        elif opcion == "2":
            gestionar_tipo_vehiculo()
        elif opcion == "3":
            gestionar_vehiculo()
        elif opcion == "4":
            gestionar_registro()
        elif opcion == "5":
            gestionar_rol_empleado()
        elif opcion == "6":
            gestionar_empleado()
        elif opcion == "7":
            gestionar_metodoPago() 
        elif opcion == "8":
            gestionar_pago()        
        elif opcion == "9":
            gestionar_tarifa()  
        elif opcion == "10":
            gestionar_incidente()
        elif opcion == "11":
            gestionar_promocion()
        elif opcion == "12":
            gestionar_membresia() 
        elif opcion == "13":
            gestionar_multa() 
        elif opcion == "14":
            gestionar_factura()   
        elif opcion == "15":
            gestionar_gasto()            
        elif opcion == "16":
            print("Saliendo del sistema...")
            break        
        else:
            print("Opción no válida. Intente nuevamente.")
