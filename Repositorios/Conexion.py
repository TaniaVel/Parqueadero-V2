import pyodbc
from Entidades import Cliente

class Conexion:
    cadena_conexion = (
        "Driver={MySQL ODBC 9.4 Unicode Driver};"
        "Server=localhost;"
        "Database=db_parqueadero2;"
        "Port=3306;"
        "User=user_python;"
        "Password=123456;"
    )

    # ========================
    #  MÉTODO SELECT
    # ========================
    def CargarClientes(self) -> None:
        conexion = pyodbc.connect(self.cadena_conexion)
        cursor = conexion.cursor()

        consulta: str = """ {CALL proc_select_clientes();} """
        cursor.execute(consulta)

        lista: list = []
        for elemento in cursor:
            entidad = Cliente.Cliente()
            entidad.SetIdCliente(elemento[0])
            entidad.SetNombre(elemento[1])
            entidad.SetDocumento(elemento[2])
            entidad.SetTelefono(elemento[3])
            entidad.SetCorreo(elemento[4])
            entidad.SetDireccion(elemento[5])
            lista.append(entidad)

        cursor.close()
        conexion.close()

        for c in lista:
            print(f"{c.GetIdCliente()} - {c.GetNombre()} - {c.GetDocumento()} - {c.GetTelefono()}")

    # ========================
    #  MÉTODO INSERT
    # ========================
    def InsertarCliente(self, nombre, documento, telefono, correo, direccion):
        try:
            conexion = pyodbc.connect(self.cadena_conexion)
            cursor = conexion.cursor()

            consulta = """{CALL proc_insert_clientes(?, ?, ?, ?, ?)}"""
            cursor.execute(consulta, (nombre, documento, telefono, correo, direccion))
            conexion.commit()
            print(f" Cliente '{nombre}' insertado correctamente")

            cursor.close()
            conexion.close()
        except Exception as e:
            print("Error al insertar cliente:", e)

    # ========================
    #  MÉTODO UPDATE
    # ========================
    def ActualizarCliente(self, id_cliente, nombre, documento, telefono, correo, direccion):
        try:
            conexion = pyodbc.connect(self.cadena_conexion)
            cursor = conexion.cursor()

            consulta = """{CALL proc_update_clientes(?, ?, ?, ?, ?, ?)}"""
            cursor.execute(consulta, (id_cliente, nombre, documento, telefono, correo, direccion))
            conexion.commit()
            print(f"Cliente con ID {id_cliente} actualizado correctamente")

            cursor.close()
            conexion.close()
        except Exception as e:
            print("Error al actualizar cliente:", e)

    # ========================
    #  MÉTODO DELETE
    # ========================
    def EliminarCliente(self, id_cliente):
        try:
            conexion = pyodbc.connect(self.cadena_conexion)
            cursor = conexion.cursor()

            consulta = """{CALL proc_delete_clientes(?)}"""
            cursor.execute(consulta, (id_cliente,))
            conexion.commit()
            print(f"Cliente con ID {id_cliente} eliminado correctamente")

            cursor.close()
            conexion.close()
        except Exception as e:
            print("Error al eliminar cliente:", e)
