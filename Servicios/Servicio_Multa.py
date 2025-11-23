from Repositorios.Cone_Multa import Conexion_Multa
from Utilidades.Convertir_Json import multas_to_json

class Servicio_Multa:

    # ✅ GET - Cargar multas
    def CargarMultas(self) -> dict:

        conexion = Conexion_Multa()
        lista = conexion.CargarMultas()

        return multas_to_json(lista)

    # ✅ POST - Insertar multa
    def InsertarMulta(self, data: dict):

        conexion = Conexion_Multa()
        conexion.InsertarMulta(self.__crear_multa(data))

        return "Multa registrada correctamente"

    # ✅ PUT - Actualizar multa
    def ActualizarMulta(self, data: dict):

        conexion = Conexion_Multa()
        multa = self.__crear_multa(data)
        multa.SetIdMulta(data["IdMulta"])

        conexion.ActualizarMulta(multa)

        return "Multa actualizada correctamente"

    # ✅ DELETE - Eliminar multa
    def EliminarMulta(self, id_multa: int):

        conexion = Conexion_Multa()
        conexion.EliminarMulta(id_multa)

        return "Multa eliminada correctamente"

    # ✅ Método interno para crear entidad Multa
    def __crear_multa(self, data):

        from Entidades.Multa import Multa

        m = Multa()
        m.SetIdRegistro(data["IdRegistro"])
        m.SetMotivo(data["Motivo"])
        m.SetValor(data["Valor"])
        m.SetFecha(data["Fecha"])

        return m
