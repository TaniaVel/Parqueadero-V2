import pyodbc
from Entidades.Cliente import Cliente
from Repositorios.Conexion import Conexion


class Conexion_Cliente(Conexion):

    def CargarClientes(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_clientes()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay clientes registrados en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                c = Cliente()
                c.SetIdCliente(elemento[0])
                c.SetNombre(elemento[1])
                c.SetDocumento(elemento[2])
                c.SetTelefono(elemento[3])
                c.SetCorreo(elemento[4])
                c.SetDireccion(elemento[5])
                lista.append(c)

            return lista

        except Exception as e:
            print("\nError al cargar clientes:", e)
            return []

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def InsertarCliente(self, cliente: Cliente):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_clientes(?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                cliente.GetNombre(),
                cliente.GetDocumento(),
                cliente.GetTelefono(),
                cliente.GetCorreo(),
                cliente.GetDireccion()
            ))
            conexion.commit()
            print(f"\nCliente '{cliente.GetNombre()}' insertado correctamente")

        except pyodbc.IntegrityError as e:
            if "Duplicate entry" in str(e):
                print(f"\nError: El documento '{cliente.GetDocumento()}' ya existe en la base de datos.")
            else:
                print("\nError de integridad:", e)

        except Exception as e:
            # Cualquier otro error
            print("\nError al insertar cliente:", e)

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def ActualizarCliente(self, cliente: Cliente):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_cliente_por_id(?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                cliente.GetIdCliente(),
                cliente.GetNombre(),
                cliente.GetTelefono(),
                cliente.GetCorreo(),
                cliente.GetDireccion()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl cliente con ID {cliente.GetIdCliente()} no existe o no hubo cambios. No se actualizó información.")
            else:
                print(f"\nCliente ID {cliente.GetIdCliente()} actualizado correctamente")

        except Exception as e:
            print(f"\nError al actualizar cliente: {e}")

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()


    def EliminarCliente(self, id_cliente: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_clientes(?)}"
            cursor.execute(consulta, (id_cliente,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl cliente con ID {id_cliente} no existe. No se eliminó información.")
            else:
                print(f"\nCliente ID {id_cliente} eliminado correctamente")

        except Exception as e:
            print(f"\nError al eliminar cliente: {e}")

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()