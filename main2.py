from Repositorios import Conexion

db = Conexion.Conexion()

print("Insertando nuevo cliente...")
db.InsertarCliente("Juan Torres", "1001234567", "3104567890", "juan.torres@gmail.com", "Calle 50 #10-22")

print("Actualizando cliente con id 1...")
db.ActualizarCliente(1, "Laura Gómez", "1009876543", "3112223344", "laura.gomez@gmail.com", "Av 80 #12-45")

print("Eliminando cliente con id 2...")
db.EliminarCliente(2)

print("Cargando todos los clientes...")
db.CargarClientes()


