class TipoVehiculo:
    id_tipo: int = 0
    nombre: str = None
    descripcion: str = None

    def GetIdTipo(self): return self.id_tipo
    def SetIdTipo(self, value: int): self.id_tipo = value

    def GetNombre(self): return self.nombre
    def SetNombre(self, value: str): self.nombre = value

    def GetDescripcion(self): return self.descripcion
    def SetDescripcion(self, value: str): self.descripcion = value
