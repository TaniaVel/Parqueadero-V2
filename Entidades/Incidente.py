class Incidente:
    id_incidente: int = 0
    id_registro: int = 0
    descripcion: str = None
    fecha: str = None
    id_empleado: int = 0

    def GetIdIncidente(self): return self.id_incidente
    def SetIdIncidente(self, value: int): self.id_incidente = value

    def GetIdRegistro(self): return self.id_registro
    def SetIdRegistro(self, value: int): self.id_registro = value

    def GetDescripcion(self): return self.descripcion
    def SetDescripcion(self, value: str): self.descripcion = value

    def GetFecha(self): return self.fecha
    def SetFecha(self, value: str): self.fecha = value

    def GetIdEmpleado(self): return self.id_empleado
    def SetIdEmpleado(self, value: int): self.id_empleado = value
