class Empleado:
    id_empleado: int = 0
    nombre: str = None
    documento: str = None
    telefono: str = None
    correo: str = None
    id_rol: int = 0

    def GetIdEmpleado(self): return self.id_empleado
    def SetIdEmpleado(self, value: int): self.id_empleado = value

    def GetNombre(self): return self.nombre
    def SetNombre(self, value: str): self.nombre = value

    def GetDocumento(self): return self.documento
    def SetDocumento(self, value: str): self.documento = value

    def GetTelefono(self): return self.telefono
    def SetTelefono(self, value: str): self.telefono = value

    def GetCorreo(self): return self.correo
    def SetCorreo(self, value: str): self.correo = value

    def GetIdRol(self): return self.id_rol
    def SetIdRol(self, value: int): self.id_rol = value
