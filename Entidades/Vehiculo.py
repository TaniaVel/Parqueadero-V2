class Vehiculo:
    id_vehiculo: int = 0
    placa: str = None
    marca: str = None
    color: str = None
    id_tipo: int = 0
    id_cliente: int = 0

    def GetIdVehiculo(self): return self.id_vehiculo
    def SetIdVehiculo(self, value: int): self.id_vehiculo = value

    def GetPlaca(self): return self.placa
    def SetPlaca(self, value: str): self.placa = value

    def GetMarca(self): return self.marca
    def SetMarca(self, value: str): self.marca = value

    def GetColor(self): return self.color
    def SetColor(self, value: str): self.color = value

    def GetIdTipo(self): return self.id_tipo
    def SetIdTipo(self, value: int): self.id_tipo = value

    def GetIdCliente(self): return self.id_cliente
    def SetIdCliente(self, value: int): self.id_cliente = value
