from Repositorios.Cone_Registro import Conexion_Registro
from Utilidades.Convertir_Json import entradasalida_to_json

class Servicio_EntradaSalida:

    # GET - Cargar todos los registros
    def CargarRegistros(self) -> dict:

        conexion = Conexion_Registro()
        lista = conexion.CargarRegistros()

        return entradasalida_to_json(lista)

    # POST - Insertar registro
    def InsertarRegistro(self, data: dict):

        conexion = Conexion_Registro()
        conexion.InsertarRegistro(self.__crear_registro_entrada(data))

        return "Proceso ejecutado. Ver detalles en servidor"

    # PUT - Actualizar registro
    def ActualizarRegistro(self, data: dict):

        conexion = Conexion_Registro()
        registro = self.__crear_registro(data)
        registro.SetIdRegistro(data["IdRegistro"])

        conexion.ActualizarRegistro(registro)

        return "Proceso ejecutado. Ver detalles en servidor"

    # DELETE - Eliminar registro
    def EliminarRegistro(self, id_registro: int):

        conexion = Conexion_Registro()
        conexion.EliminarRegistro(id_registro)

        return "Proceso ejecutado. Ver detalles en servidor"

    # Método para registrar entrada
    def __crear_registro_entrada(self, data):

        from Entidades.Entradasalida import Entradasalida

        reg = Entradasalida()
        reg.SetIdVehiculo(data["IdVehiculo"])
        reg.SetIdEmpleado(data["IdEmpleado"])
        reg.SetFechaEntrada(data["FechaEntrada"])
        reg.SetEspacio(data["Espacio"])

        return reg

    #  Método interno para  registro completo
    def __crear_registro(self, data):

        from Entidades.Entradasalida import Entradasalida

        reg = Entradasalida()
        reg.SetIdVehiculo(data["IdVehiculo"])
        reg.SetIdEmpleado(data["IdEmpleado"])
        reg.SetFechaEntrada(data["FechaEntrada"])
        reg.SetFechaSalida(data["FechaSalida"])
        reg.SetEspacio(data["Espacio"])

        return reg
