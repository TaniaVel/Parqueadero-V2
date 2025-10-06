class Factura:
    id_factura: int = 0
    id_pago: int = 0
    numero_factura: str = None
    fecha_emision: str = None
    total: float = 0.0

    def GetIdFactura(self): return self.id_factura
    def SetIdFactura(self, value: int): self.id_factura = value

    def GetIdPago(self): return self.id_pago
    def SetIdPago(self, value: int): self.id_pago = value

    def GetNumeroFactura(self): return self.numero_factura
    def SetNumeroFactura(self, value: str): self.numero_factura = value

    def GetFechaEmision(self): return self.fecha_emision
    def SetFechaEmision(self, value: str): self.fecha_emision = value

    def GetTotal(self): return self.total
    def SetTotal(self, value: float): self.total = value
