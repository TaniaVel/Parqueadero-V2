from Repositorios.Cone_Pago import Conexion_Pago
from Utilidades.Convertir_Json import pagos_to_json

class Servicio_Pago:

    # ✅ GET - Cargar pagos
    def CargarPagos(self) -> dict:

        conexion = Conexion_Pago()
        lista = conexion.CargarPagos()

        return pagos_to_json(lista)

    # ✅ POST - Insertar pago
    def InsertarPago(self, data: dict):

        conexion = Conexion_Pago()
        conexion.InsertarPago(self.__crear_pago(data))

        return "Pago registrado correctamente"

    # ✅ PUT - Actualizar pago
    def ActualizarPago(self, data: dict):

        conexion = Conexion_Pago()
        pago = self.__crear_pago(data)
        pago.SetIdPago(data["IdPago"])

        conexion.ActualizarPago(pago)

        return "Pago actualizado correctamente"

    # ✅ DELETE - Eliminar pago
    def EliminarPago(self, id_pago: int):

        conexion = Conexion_Pago()
        conexion.EliminarPago(id_pago)

        return "Pago eliminado correctamente"

    # ✅ Método interno para crear entidad Pago
    def __crear_pago(self, data):

        from Entidades.Pago import Pago

        p = Pago()
        p.SetIdRegistro(data["IdRegistro"])
        p.SetIdMetodo(data["IdMetodo"])
        p.SetMonto(data["Monto"])
        p.SetFechaPago(data["FechaPago"])
        p.SetIdEmpleado(data["IdEmpleado"])

        return p
