class Membresia:
    id_membresia: int = 0
    id_cliente: int = 0
    fecha_inicio: str = None
    fecha_fin: str = None
    tipo: str = None
    descuento: float = 0.0
    estado: str = None

    def GetIdMembresia(self): return self.id_membresia
    def SetIdMembresia(self, value: int): self.id_membresia = value

    def GetIdCliente(self): return self.id_cliente
    def SetIdCliente(self, value: int): self.id_cliente = value

    def GetFechaInicio(self): return self.fecha_inicio
    def SetFechaInicio(self, value: str): self.fecha_inicio = value

    def GetFechaFin(self): return self.fecha_fin
    def SetFechaFin(self, value: str): self.fecha_fin = value

    def GetTipo(self): return self.tipo
    def SetTipo(self, value: str): self.tipo = value

    def GetDescuento(self): return self.descuento
    def SetDescuento(self, value: float): self.descuento = value

    def GetEstado(self): return self.estado
    def SetEstado(self, value: str): self.estado = value