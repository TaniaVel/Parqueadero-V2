from Repositorios.Cone_Cliente import Conexion_Cliente
from Utilidades.Convertir_Json import clientes_to_json
from Seguridad.encriptador_datos import encrypt_list

class Servicio_Cliente:

    # GET - Cargar lista Clientes encriptando datos sensibles
    def CargarClientes2(self) -> dict:
        conexion = Conexion_Cliente()
        lista = conexion.CargarClientes()
        json_data = clientes_to_json(lista)
        json_data = encrypt_list(json_data)
        
        return json_data

    # GET - Cargar lista Clientes

    def CargarClientes(self) -> dict:
        conexion = Conexion_Cliente()
        lista = conexion.CargarClientes()

        return clientes_to_json(lista)

    # POST - Insertar cLIENTE
    def InsertarCliente(self, data: dict):

        conexion = Conexion_Cliente()
        conexion.InsertarCliente(self.__crear_cliente(data))

        return "Proceso ejecutado. Ver detalles en servidor"

    # PUT - Actualizar Cliente
    def ActualizarCliente(self, data: dict):

        conexion = Conexion_Cliente()
        cliente = self.__crear_cliente(data)
        cliente.SetIdCliente(data["IdCliente"])

        conexion.ActualizarCliente(cliente)
        return "Proceso ejecutado. Ver detalles en servidor"

    # DELETE - Eliminar empleado
    def EliminarCliente(self, id_cliente: int):

        conexion = Conexion_Cliente()
        conexion.EliminarCliente(id_cliente)

        return "Proceso ejecutado. Ver detalles en servidor"
    
     # Método Crear empleado   
    def __crear_cliente(self, data):

        from Entidades.Cliente import Cliente

        cli = Cliente()
        cli.SetNombre(data["Nombre"])
        cli.SetDocumento(data["Documento"])
        cli.SetTelefono(data["Telefono"])
        cli.SetCorreo(data["Correo"])
        cli.SetDireccion(data["Direccion"])

        return cli
