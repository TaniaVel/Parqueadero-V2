from Repositorios.Cone_Tarifa import Conexion_Tarifa
from Utilidades.Convertir_Json import tarifas_to_json

class Servicio_Tarifa:

    # GET - Cargar tarifas
    def CargarTarifas(self) -> dict:
        conexion = Conexion_Tarifa()
        lista = conexion.CargarTarifas()

        return tarifas_to_json(lista)

    # POST - Insertar tarifa
    def InsertarTarifa(self, data: dict):

        conexion = Conexion_Tarifa()
        conexion.InsertarTarifa(self.__crear_tarifa(data))

        return "Proceso ejecutado. Ver detalles en servidor"

    # PUT - Actualizar tarifa
    def ActualizarTarifa(self, data: dict):

        conexion = Conexion_Tarifa()
        tarifa = self.__crear_tarifa(data)
        tarifa.SetIdTarifa(data["IdTarifa"])

        conexion.ActualizarTarifa(tarifa)

        return "Proceso ejecutado. Ver detalles en servidor"

    # DELETE - Eliminar tarifa
    def EliminarTarifa(self, id_tarifa: int):

        conexion = Conexion_Tarifa()
        conexion.EliminarTarifa(id_tarifa)

        return "Proceso ejecutado. Ver detalles en servidor"

    # Método interno
    def __crear_tarifa(self, data):

        from Entidades.Tarifa import Tarifa

        t = Tarifa()
        t.SetIdTipo(data["IdTipo"])
        t.SetTipoTarifa(data["TipoTarifa"])
        t.SetValor(data["Valor"])

        return t
