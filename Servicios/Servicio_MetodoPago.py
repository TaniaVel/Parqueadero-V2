from Repositorios.Cone_MetodoPago import Conexion_MetodoPago
from Utilidades.Convertir_Json import metodos_to_json

class Servicio_MetodoPago:

    # GET - Cargar métodos
    def CargarMetodos(self) -> dict:

        conexion = Conexion_MetodoPago()
        lista = conexion.CargarMetodos()

        return metodos_to_json(lista)

    # POST - Insertar método
    def InsertarMetodo(self, data: dict):

        conexion = Conexion_MetodoPago()
        conexion.InsertarMetodo(self.__crear_metodo(data))

        return "Proceso ejecutado. Ver detalles en servidor"

    # PUT - Actualizar método
    def ActualizarMetodo(self, data: dict):

        conexion = Conexion_MetodoPago()
        metodo = self.__crear_metodo(data)
        metodo.SetIdMetodo(data["IdMetodo"])

        conexion.ActualizarMetodo(metodo)

        return "Proceso ejecutado. Ver detalles en servidor"

    # DELETE - Eliminar método
    def EliminarMetodo(self, id_metodo: int):

        conexion = Conexion_MetodoPago()
        conexion.EliminarMetodo(id_metodo)

        return "Proceso ejecutado. Ver detalles en servidor"

    # Crear método de pago
    def __crear_metodo(self, data):

        from Entidades.MetodoPago import MetodoPago

        m = MetodoPago()
        m.SetNombre(data["Nombre"])
        m.SetDescripcion(data["Descripcion"])

        return m
