class Entradasalida:
    id_registro: int = 0
    id_vehiculo: int = 0
    id_empleado: int = 0
    fecha_entrada: str = None
    fecha_salida: str = None
    espacio: str = None

    def GetIdRegistro(self): return self.id_registro
    def SetIdRegistro(self, value: int): self.id_registro = value

    def GetIdVehiculo(self): return self.id_vehiculo
    def SetIdVehiculo(self, value: int): self.id_vehiculo = value

    def GetIdEmpleado(self): return self.id_empleado
    def SetIdEmpleado(self, value: int): self.id_empleado = value

    def GetFechaEntrada(self): return self.fecha_entrada
    def SetFechaEntrada(self, value: str): self.fecha_entrada = value

    def GetFechaSalida(self): return self.fecha_salida
    def SetFechaSalida(self, value: str): self.fecha_salida = value

    def GetEspacio(self): return self.espacio
    def SetEspacio(self, value: str): self.espacio = value