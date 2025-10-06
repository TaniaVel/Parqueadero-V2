class MetodoPago:
    id_metodo: int = 0
    nombre: str = None
    descripcion: str = None

    def GetIdMetodo(self): return self.id_metodo
    def SetIdMetodo(self, value: int): self.id_metodo = value

    def GetNombre(self): return self.nombre
    def SetNombre(self, value: str): self.nombre = value

    def GetDescripcion(self): return self.descripcion
    def SetDescripcion(self, value: str): self.descripcion = value
