class Tarifa:
    id_tarifa: int = 0
    id_tipo: int = 0
    tipo_tarifa: str = None
    valor: float = 0.0

    def GetIdTarifa(self): return self.id_tarifa
    def SetIdTarifa(self, value: int): self.id_tarifa = value

    def GetIdTipo(self): return self.id_tipo
    def SetIdTipo(self, value: int): self.id_tipo = value

    def GetTipoTarifa(self): return self.tipo_tarifa
    def SetTipoTarifa(self, value: str): self.tipo_tarifa = value

    def GetValor(self): return self.valor
    def SetValor(self, value: float): self.valor = value