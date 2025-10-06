import pyodbc

class Conexion:
    def __init__(self):
        self.cadena_conexion = (
            "Driver={MySQL ODBC 9.4 Unicode Driver};"
            "Server=localhost;"
            "Database=db_parqueadero2;"
            "Port=3306;"
            "User=user_python;"
            "Password=123456;"
        )

    def get_conexion(self):
        
        return pyodbc.connect(self.cadena_conexion)
