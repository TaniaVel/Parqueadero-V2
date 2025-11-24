
class ClienteJSON:

    def Convertir(cliente) -> dict:
        return {
            "IdCliente": cliente.GetIdCliente(),
            "Nombre": cliente.GetNombre(),
            "Documento": cliente.GetDocumento(),
            "Telefono": cliente.GetTelefono(),
            "Correo": cliente.GetCorreo(),
            "Direccion": cliente.GetDireccion()
        }
