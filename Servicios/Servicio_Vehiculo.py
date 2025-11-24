from Repositorios.Cone_Vehiculo import Conexion_Vehiculo
from Utilidades.Convertir_Json import vehiculos_to_json

class Servicio_Vehiculo:

    # GET - Cargar vehículos
    def CargarVehiculos(self) -> dict:
        conexion = Conexion_Vehiculo()
        lista = conexion.CargarVehiculos()

        return vehiculos_to_json(lista)

    # POST - Insertar vehículo
    def InsertarVehiculo(self, data: dict):

        conexion = Conexion_Vehiculo()
        conexion.InsertarVehiculo(self.__crear_vehiculo(data))

        return "Vehículo insertado correctamente"

    # PUT - Actualizar vehículo
    def ActualizarVehiculo(self, data: dict):

        conexion = Conexion_Vehiculo()
        vehiculo = self.__crear_vehiculo(data)
        vehiculo.SetIdVehiculo(data["IdVehiculo"])

        conexion.ActualizarVehiculo(vehiculo)

        return "Vehículo actualizado correctamente"

    # DELETE - Eliminar vehículo
    def EliminarVehiculo(self, id_vehiculo: int):

        conexion = Conexion_Vehiculo()
        conexion.EliminarVehiculo(id_vehiculo)

        return "Vehículo eliminado correctamente"

    # Método  para crear  Vehiculo
    def __crear_vehiculo(self, data):

        from Entidades.Vehiculo import Vehiculo

        v = Vehiculo()
        v.SetPlaca(data["Placa"])
        v.SetMarca(data["Marca"])
        v.SetColor(data["Color"])
        v.SetIdTipo(data["IdTipo"])
        v.SetIdCliente(data["IdCliente"])

        return v
