class Pago:
    id_pago: int = 0
    id_registro: int = 0
    id_metodo: int = 0
    monto: float = 0.0
    fecha_pago: str = None
    id_empleado: int = 0

    def GetIdPago(self): return self.id_pago
    def SetIdPago(self, value: int): self.id_pago = value

    def GetIdRegistro(self): return self.id_registro
    def SetIdRegistro(self, value: int): self.id_registro = value

    def GetIdMetodo(self): return self.id_metodo
    def SetIdMetodo(self, value: int): self.id_metodo = value

    def GetMonto(self): return self.monto
    def SetMonto(self, value: float): self.monto = value

    def GetFechaPago(self): return self.fecha_pago
    def SetFechaPago(self, value: str): self.fecha_pago = value

    def GetIdEmpleado(self): return self.id_empleado
    def SetIdEmpleado(self, value: int): self.id_empleado = value
