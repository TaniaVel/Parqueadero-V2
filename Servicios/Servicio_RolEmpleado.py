from Repositorios.Cone_RolEmpleado import Conexion_RolEmpleado
from Utilidades.Convertir_Json import roles_to_json

class Servicio_RolEmpleado:

    # GET - Cargar roles
    def CargarRoles(self) -> dict:
        conexion = Conexion_RolEmpleado()
        lista = conexion.CargarRoles()

        return roles_to_json(lista)

    #  POST - Insertar rol
    def InsertarRol(self, data: dict):

        conexion = Conexion_RolEmpleado()
        conexion.InsertarRol(self.__crear_rol(data))

        return "Rol insertado correctamente"

    #  PUT - Actualizar rol
    def ActualizarRol(self, data: dict):

        conexion = Conexion_RolEmpleado()
        rol = self.__crear_rol(data)
        rol.SetIdRol(data["IdRol"])

        conexion.ActualizarRol(rol)

        return "Rol actualizado correctamente"

    #  DELETE - Eliminar rol
    def EliminarRol(self, id_rol: int):

        conexion = Conexion_RolEmpleado()
        conexion.EliminarRol(id_rol)

        return "Rol eliminado correctamente"

    #  Método interno para crear entidad RolEmpleado
    def __crear_rol(self, data):

        from Entidades.RolEmpleado import RolEmpleado

        r = RolEmpleado()
        r.SetNombre(data["Nombre"])
        r.SetDescripcion(data["Descripcion"])

        return r
