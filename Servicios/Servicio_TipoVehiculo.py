from Repositorios.Cone_TipoVehiculo import Conexion_TipoVehiculo
from Utilidades.Convertir_Json import tiposvehiculo_to_json

class Servicio_TipoVehiculo:

    def CargarTipoVehiculos(self) -> dict:

        conexion = Conexion_TipoVehiculo()
        lista = conexion.CargarTipoVehiculos()

        return tiposvehiculo_to_json(lista)

    def InsertarTipoVehiculo(self, data: dict):

        conexion = Conexion_TipoVehiculo()
        conexion.InsertarTipoVehiculo(self.__crear_tipo(data))

        return "TipoVehiculo insertado correctamente"

    def ActualizarTipoVehiculo(self, data: dict):

        conexion = Conexion_TipoVehiculo()
        tipo = self.__crear_tipo(data)
        tipo.SetIdTipo(data["IdTipo"])

        conexion.ActualizarTipoVehiculo(tipo)
        return "TipoVehiculo actualizado correctamente"

    def EliminarTipoVehiculo(self, id_tipo: int):

        conexion = Conexion_TipoVehiculo()
        conexion.EliminarTipoVehiculo(id_tipo)

        return "TipoVehiculo eliminado correctamente"

    # ✅ Método interno para crear entidad
    def __crear_tipo(self, data):

        from Entidades.TipoVehiculo import TipoVehiculo

        tv = TipoVehiculo()
        tv.SetNombre(data["Nombre"])
        tv.SetDescripcion(data["Descripcion"])

        return tv
