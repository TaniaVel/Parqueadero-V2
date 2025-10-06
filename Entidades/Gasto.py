class Gasto:
    id_gasto: int = 0
    descripcion: str = None
    monto: float = 0.0
    fecha: str = None
    id_empleado: int = 0

    def GetIdGasto(self): return self.id_gasto
    def SetIdGasto(self, value: int): self.id_gasto = value

    def GetDescripcion(self): return self.descripcion
    def SetDescripcion(self, value: str): self.descripcion = value

    def GetMonto(self): return self.monto
    def SetMonto(self, value: float): self.monto = value

    def GetFecha(self): return self.fecha
    def SetFecha(self, value: str): self.fecha = value

    def GetIdEmpleado(self): return self.id_empleado
    def SetIdEmpleado(self, value: int): self.id_empleado = value