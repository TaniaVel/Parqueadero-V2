import pyodbc
from Entidades.Vehiculo import Vehiculo
from Repositorios.Conexion import Conexion


class Conexion_Vehiculo(Conexion):

    def CargarVehiculos(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_vehiculos()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay vehículos registrados en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                v = Vehiculo()
                v.SetIdVehiculo(elemento[0])
                v.SetPlaca(elemento[1])
                v.SetMarca(elemento[2])
                v.SetColor(elemento[3])
                v.SetIdTipo(elemento[4])
                v.SetIdCliente(elemento[5])
                lista.append(v)

            return lista

        except Exception as e:
            print("\nError al cargar vehículos:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    def InsertarVehiculo(self, vehiculo: Vehiculo):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_vehiculo(?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                vehiculo.GetPlaca(),
                vehiculo.GetMarca(),
                vehiculo.GetColor(),
                vehiculo.GetIdTipo(),
                vehiculo.GetIdCliente()
            ))
            conexion.commit()
            print(f"\nVehículo '{vehiculo.GetPlaca()}' insertado correctamente")

        except pyodbc.IntegrityError as e:
            if "Duplicate entry" in str(e):
                print(f"\nError: La placa '{vehiculo.GetPlaca()}' ya existe en la base de datos.")
            else:
                print("\nError de integridad:", e)

        except Exception as e:
            print("\nError al insertar vehículo:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    def ActualizarVehiculo(self, vehiculo: Vehiculo):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_vehiculo_por_id(?, ?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                vehiculo.GetIdVehiculo(),
                vehiculo.GetPlaca(),
                vehiculo.GetMarca(),
                vehiculo.GetColor(),
                vehiculo.GetIdTipo(),
                vehiculo.GetIdCliente()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl vehículo con ID {vehiculo.GetIdVehiculo()} no existe o no hubo cambios. No se actualizó información.")
            else:
                print(f"\nVehículo ID {vehiculo.GetIdVehiculo()} actualizado correctamente")

        except Exception as e:
            print(f"\nError al actualizar vehículo: {e}")

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    def EliminarVehiculo(self, id_vehiculo: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_vehiculo(?)}"
            cursor.execute(consulta, (id_vehiculo,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl vehículo con ID {id_vehiculo} no existe. No se eliminó información.")
            else:
                print(f"\nVehículo ID {id_vehiculo} eliminado correctamente")

        except Exception as e:
            print(f"\nError al eliminar vehículo: {e}")

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
