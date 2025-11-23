from Repositorios.Cone_Incidente import Conexion_Incidente
from Utilidades.Convertir_Json import incidentes_to_json

class Servicio_Incidente:

    # ✅ GET - Cargar incidentes
    def CargarIncidentes(self) -> dict:

        conexion = Conexion_Incidente()
        lista = conexion.CargarIncidentes()

        return incidentes_to_json(lista)

    # ✅ POST - Insertar incidente
    def InsertarIncidente(self, data: dict):

        conexion = Conexion_Incidente()
        conexion.InsertarIncidente(self.__crear_incidente(data))

        return "Incidente registrado correctamente"

    # ✅ PUT - Actualizar incidente
    def ActualizarIncidente(self, data: dict):

        conexion = Conexion_Incidente()
        incidente = self.__crear_incidente(data)
        incidente.SetIdIncidente(data["IdIncidente"])

        conexion.ActualizarIncidente(incidente)

        return "Incidente actualizado correctamente"

    # ✅ DELETE - Eliminar incidente
    def EliminarIncidente(self, id_incidente: int):

        conexion = Conexion_Incidente()
        conexion.EliminarIncidente(id_incidente)

        return "Incidente eliminado correctamente"

    # ✅ Método interno para crear entidad Incidente
    def __crear_incidente(self, data):

        from Entidades.Incidente import Incidente

        i = Incidente()
        i.SetIdRegistro(data["IdRegistro"])
        i.SetDescripcion(data["Descripcion"])
        i.SetFecha(data["Fecha"])
        i.SetIdEmpleado(data["IdEmpleado"])

        return i
