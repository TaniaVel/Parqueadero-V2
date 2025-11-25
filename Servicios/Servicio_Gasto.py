from Repositorios.Cone_Gasto import Conexion_Gasto
from Utilidades.Convertir_Json import gastos_to_json

class Servicio_Gasto:

    # GET - Cargar gastos
    def CargarGastos(self) -> dict:

        conexion = Conexion_Gasto()
        lista = conexion.CargarGastos()

        return gastos_to_json(lista)

    # POST - Insertar gasto
    def InsertarGasto(self, data: dict):

        conexion = Conexion_Gasto()
        conexion.InsertarGasto(self.__crear_gasto(data))

        return "Proceso ejecutado. Ver detalles en servidor"

    # PUT - Actualizar gasto
    def ActualizarGasto(self, data: dict):

        conexion = Conexion_Gasto()
        gasto = self.__crear_gasto(data)
        gasto.SetIdGasto(data["IdGasto"])

        conexion.ActualizarGasto(gasto)

        return "Proceso ejecutado. Ver detalles en servidor"

    # DELETE - Eliminar gasto
    def EliminarGasto(self, id_gasto: int):

        conexion = Conexion_Gasto()
        conexion.EliminarGasto(id_gasto)

        return "Proceso ejecutado. Ver detalles en servidor"

    # Método  para crear Gasto
    def __crear_gasto(self, data):

        from Entidades.Gasto import Gasto

        g = Gasto()
        g.SetDescripcion(data["Descripcion"])
        g.SetMonto(data["Monto"])
        g.SetFecha(data["Fecha"])
        g.SetIdEmpleado(data["IdEmpleado"])

        return g
