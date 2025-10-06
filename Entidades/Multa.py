class Multa:
    id_multa: int = 0
    id_registro: int = 0
    motivo: str = None
    valor: float = 0.0
    fecha: str = None

    def GetIdMulta(self): return self.id_multa
    def SetIdMulta(self, value: int): self.id_multa = value

    def GetIdRegistro(self): return self.id_registro
    def SetIdRegistro(self, value: int): self.id_registro = value

    def GetMotivo(self): return self.motivo
    def SetMotivo(self, value: str): self.motivo = value

    def GetValor(self): return self.valor
    def SetValor(self, value: float): self.valor = value

    def GetFecha(self): return self.fecha
    def SetFecha(self, value: str): self.fecha = value