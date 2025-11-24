from Repositorios.Cone_Factura import Conexion_Factura
from Utilidades.Convertir_Json import facturas_to_json

class Servicio_Factura:

    #  GET - Cargar facturas
    def CargarFacturas(self) -> dict:

        conexion = Conexion_Factura()
        lista = conexion.CargarFacturas()

        return facturas_to_json(lista)

    #  POST - Insertar factura
    def InsertarFactura(self, data: dict):

        conexion = Conexion_Factura()
        conexion.InsertarFactura(self.__crear_factura(data))

        return "Factura registrada correctamente"

    #  PUT - Actualizar factura
    def ActualizarFactura(self, data: dict):

        conexion = Conexion_Factura()
        factura = self.__crear_factura(data)
        factura.SetIdFactura(data["IdFactura"])

        conexion.ActualizarFactura(factura)

        return "Factura actualizada correctamente"

    # DELETE - Eliminar factura
    def EliminarFactura(self, id_factura: int):

        conexion = Conexion_Factura()
        conexion.EliminarFactura(id_factura)

        return "Factura eliminada correctamente"

    # Método para crear  Factura
    def __crear_factura(self, data):

        from Entidades.Factura import Factura

        f = Factura()
        f.SetIdPago(data["IdPago"])
        f.SetNumeroFactura(data["NumeroFactura"])
        f.SetFechaEmision(data["FechaEmision"])
        f.SetTotal(data["Total"])

        return f
