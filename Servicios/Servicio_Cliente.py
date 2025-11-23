from Repositorios.Cone_Cliente import Conexion_Cliente
from Utilidades.Convertir_Json import clientes_to_json

class Servicio_Cliente:

    def CargarClientes(self) -> dict:
        conexion = Conexion_Cliente()
        lista = conexion.CargarClientes()

        return clientes_to_json(lista)

    def InsertarCliente(self, data: dict):

        conexion = Conexion_Cliente()
        conexion.InsertarCliente(self.__crear_cliente(data))

        return "Cliente insertado correctamente"

    def ActualizarCliente(self, data: dict):

        conexion = Conexion_Cliente()
        cliente = self.__crear_cliente(data)
        cliente.SetIdCliente(data["IdCliente"])

        conexion.ActualizarCliente(cliente)
        return "Cliente actualizado correctamente"

    def EliminarCliente(self, id_cliente: int):

        conexion = Conexion_Cliente()
        conexion.EliminarCliente(id_cliente)

        return "Cliente eliminado correctamente"

    # ✅ Método interno para crear entidad Cliente
    def __crear_cliente(self, data):

        from Entidades.Cliente import Cliente

        cli = Cliente()
        cli.SetNombre(data["Nombre"])
        cli.SetDocumento(data["Documento"])
        cli.SetTelefono(data["Telefono"])
        cli.SetCorreo(data["Correo"])
        cli.SetDireccion(data["Direccion"])

        return cli
