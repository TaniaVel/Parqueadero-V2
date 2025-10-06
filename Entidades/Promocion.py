class Promocion:
    id_promocion: int = 0
    nombre: str = None
    descripcion: str = None
    descuento: float = 0.0
    fecha_inicio: str = None
    fecha_fin: str = None

    def GetIdPromocion(self): return self.id_promocion
    def SetIdPromocion(self, value: int): self.id_promocion = value

    def GetNombre(self): return self.nombre
    def SetNombre(self, value: str): self.nombre = value

    def GetDescripcion(self): return self.descripcion
    def SetDescripcion(self, value: str): self.descripcion = value

    def GetDescuento(self): return self.descuento
    def SetDescuento(self, value: float): self.descuento = value

    def GetFechaInicio(self): return self.fecha_inicio
    def SetFechaInicio(self, value: str): self.fecha_inicio = value

    def GetFechaFin(self): return self.fecha_fin
    def SetFechaFin(self, value: str): self.fecha_fin = value
