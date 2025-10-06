class RolEmpleado:
    id_rol: int = 0
    nombre: str = None
    descripcion: str = None

    def GetIdRol(self): return self.id_rol
    def SetIdRol(self, value: int): self.id_rol = value

    def GetNombre(self): return self.nombre
    def SetNombre(self, value: str): self.nombre = value

    def GetDescripcion(self): return self.descripcion
    def SetDescripcion(self, value: str): self.descripcion = value