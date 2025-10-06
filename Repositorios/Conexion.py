import pyodbc
from Entidades import Cliente

print ("entra acá")
class Conexion:
    cadena_conexion = (
        "Driver={MySQL ODBC 9.4 Unicode Driver};"
        "Server=localhost;"
        "Database=db_parqueadero2;"
        "Port=3306;"
        "User=user_python;"
        "Password=123456;"
    )

    def CargarClientes(self) -> None:
        conexion = pyodbc.connect(self.cadena_conexion)

        consulta: str = """ {CALL proc_select_clientes();} """
        cursor = conexion.cursor()
        cursor.execute(consulta)

        lista: list = []
        for elemento in cursor:
            entidad: Cliente.Cliente = Cliente.Cliente()
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
