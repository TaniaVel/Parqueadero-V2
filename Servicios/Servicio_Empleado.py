from Repositorios.Conexion_Empleado import Conexion_Empleado
from Utilidades.Convertir_Json import empleados_to_json

class Servicio_Empleado:

    # GET - Cargar lista empleados
    def CargarEmpleados(self) -> dict:
        conexion = Conexion_Empleado()
        lista = conexion.CargarEmpleados()

        return empleados_to_json(lista)

    # POST - Insertar empleado
    def InsertarEmpleado(self, data: dict):

        conexion = Conexion_Empleado()
        conexion.InsertarEmpleado(self.__crear_empleado(data))

        return "Empleado insertado correctamente"

    # PUT - Actualizar empleado
    def ActualizarEmpleado(self, data: dict):

        conexion = Conexion_Empleado()
        empleado = self.__crear_empleado(data)
        empleado.SetIdEmpleado(data["IdEmpleado"])

        conexion.ActualizarEmpleado(empleado)

        return "Empleado actualizado correctamente"

    # DELETE - Eliminar empleado
    def EliminarEmpleado(self, id_empleado: int):

        conexion = Conexion_Empleado()
        conexion.EliminarEmpleado(id_empleado)

        return "Empleado eliminado correctamente"

    # Método Crear empleado
    def __crear_empleado(self, data):

        from Entidades.Empleado import Empleado

        emp = Empleado()
        emp.SetNombre(data["Nombre"])
        emp.SetDocumento(data["Documento"])
        emp.SetTelefono(data["Telefono"])
        emp.SetCorreo(data["Correo"])
        emp.SetIdRol(data["IdRol"])

        return emp
