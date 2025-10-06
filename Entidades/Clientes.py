class Cliente:
    id_cliente: int = 0
    nombre: str = None
    documento: str = None
    telefono: str = None
    correo: str = None
    direccion: str = None

    def GetIdCliente(self): return self.id_cliente
    def SetIdCliente(self, value: int): self.id_cliente = value

    def GetNombre(self): return self.nombre
    def SetNombre(self, value: str): self.nombre = value

    def GetDocumento(self): return self.documento
    def SetDocumento(self, value: str): self.documento = value

    def GetTelefono(self): return self.telefono
    def SetTelefono(self, value: str): self.telefono = value

    def GetCorreo(self): return self.correo
    def SetCorreo(self, value: str): self.correo = value

    def GetDireccion(self): return self.direccion
    def SetDireccion(self, value: str): self.direccion = value
