from Repositorios.Cone_Cliente import Conexion_Cliente
from Entidades.Cliente import Cliente

gestion_cliente = Conexion_Cliente()

# -------------------------------
# Insertar cliente
# -------------------------------
c = Cliente()
c.SetNombre("Sara Vélez")
c.SetDocumento("987654321")  
c.SetTelefono("3111234567")
c.SetCorreo("sara@gmail.com")
c.SetDireccion("Calle 45 #12-34")
print("Insert_cliente: \n ------------")
gestion_cliente.InsertarCliente(c)

# -------------------------------
# Cargar clientes
# -------------------------------
print("Select_cliente: \n ------------")
clientes = gestion_cliente.CargarClientes()
print("Clientes actuales:")
for cl in clientes:
    print(f"{cl.GetIdCliente()} - {cl.GetNombre()} - {cl.GetDocumento()}")

# -------------------------------
# Actualizar cliente por ID
# -------------------------------
print("Update_cliente: \n ------------")
c_actualizar = Cliente()
c_actualizar.SetIdCliente(34)           
c_actualizar.SetNombre("Sara Vélez")   
c_actualizar.SetTelefono("30000000")   # número nuevo
c_actualizar.SetCorreo("sara.nuevo@gmail.com")  
c_actualizar.SetDireccion("Calle 45 #12-34")    

gestion_cliente.ActualizarCliente(c_actualizar)

# -------------------------------
# Verificación de actualización
# -------------------------------
clientes = gestion_cliente.CargarClientes()
print("\nClientes después de actualizar:")
for cl in clientes:
    print(f"{cl.GetIdCliente()} - {cl.GetNombre()} - {cl.GetDocumento()} - {cl.GetTelefono()} - {cl.GetCorreo()}")

# -------------------------------
# Eliminar cliente
# -------------------------------
print("Delete_cliente: \n ------------")
gestion_cliente.EliminarCliente(21)
