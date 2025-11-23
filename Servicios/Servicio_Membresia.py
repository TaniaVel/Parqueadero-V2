from Repositorios.Cone_Membresia import Conexion_Membresia
from Utilidades.Convertir_Json import membresias_to_json

class Servicio_Membresia:

    # ✅ GET - cargar membreías
    def CargarMembresias(self) -> dict:

        conexion = Conexion_Membresia()
        lista = conexion.CargarMembresias()

        return membresias_to_json(lista)

    # ✅ POST - insertar membresía
    def InsertarMembresia(self, data: dict):

        conexion = Conexion_Membresia()
        conexion.InsertarMembresia(self.__crear_membresia(data))

        return "Membresía registrada correctamente"

    # ✅ PUT - actualizar membresía
    def ActualizarMembresia(self, data: dict):

        conexion = Conexion_Membresia()
        membresia = self.__crear_membresia(data)
        membresia.SetIdMembresia(data["IdMembresia"])

        conexion.ActualizarMembresia(membresia)

        return "Membresía actualizada correctamente"

    # ✅ DELETE - eliminar membresía
    def EliminarMembresia(self, id_membresia: int):

        conexion = Conexion_Membresia()
        conexion.EliminarMembresia(id_membresia)

        return "Membresía eliminada correctamente"

    # ✅ Método interno para crear entidad
    def __crear_membresia(self, data):

        from Entidades.Membresia import Membresia

        m = Membresia()
        m.SetIdCliente(data["IdCliente"])
        m.SetFechaInicio(data["FechaInicio"])
        m.SetFechaFin(data["FechaFin"])
        m.SetTipo(data["Tipo"])
        m.SetDescuento(data["Descuento"])
        m.SetEstado(data["Estado"])

        return m
