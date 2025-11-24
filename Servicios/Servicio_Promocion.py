from Repositorios.Cone_Promocion import Conexion_Promocion
from Utilidades.Convertir_Json import promociones_to_json

class Servicio_Promocion:

    # GET - cargar promociones
    def CargarPromociones(self) -> dict:

        conexion = Conexion_Promocion()
        lista = conexion.CargarPromociones()

        return promociones_to_json(lista)

    # POST - insertar promoción
    def InsertarPromocion(self, data: dict):

        conexion = Conexion_Promocion()
        conexion.InsertarPromocion(self.__crear_promocion(data))

        return "Promoción registrada correctamente"

    # PUT - actualizar promoción
    def ActualizarPromocion(self, data: dict):

        conexion = Conexion_Promocion()
        promocion = self.__crear_promocion(data)
        promocion.SetIdPromocion(data["IdPromocion"])

        conexion.ActualizarPromocion(promocion)

        return "Promoción actualizada correctamente"

    # DELETE - eliminar promoción
    def EliminarPromocion(self, id_promocion: int):

        conexion = Conexion_Promocion()
        conexion.EliminarPromocion(id_promocion)

        return "Promoción eliminada correctamente"

    # Método interno para crear entidad
    def __crear_promocion(self, data):

        from Entidades.Promocion import Promocion

        p = Promocion()
        p.SetNombre(data["Nombre"])
        p.SetDescripcion(data["Descripcion"])
        p.SetDescuento(data["Descuento"])
        p.SetFechaInicio(data["FechaInicio"])
        p.SetFechaFin(data["FechaFin"])

        return p
