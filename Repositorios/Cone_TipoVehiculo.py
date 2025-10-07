import pyodbc
from Entidades.TipoVehiculo import TipoVehiculo
from Repositorios.Conexion import Conexion

class Conexion_TipoVehiculo(Conexion):

    def CargarTipoVehiculos(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_tipovehiculo()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay tipos de vehículo registrados en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                t = TipoVehiculo()
                t.SetIdTipo(elemento[0])
                t.SetNombre(elemento[1])
                t.SetDescripcion(elemento[2])
                lista.append(t)

            return lista

        except Exception as e:
            print("\nError al cargar tipos de vehículo:", e)
            return []

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def InsertarTipoVehiculo(self, tipo: TipoVehiculo):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_tipovehiculo(?, ?)}"
            cursor.execute(consulta, (tipo.GetNombre(), tipo.GetDescripcion()))
            conexion.commit()
            print(f"\nTipo de vehículo '{tipo.GetNombre()}' insertado correctamente")

        except pyodbc.IntegrityError as e:
            if "Duplicate entry" in str(e):
                print(f"\nError: El tipo de vehículo '{tipo.GetNombre()}' ya existe en la base de datos.")
            else:
                print("\nError de integridad:", e)

        except Exception as e:
            print("\nError al insertar tipo de vehículo:", e)

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def ActualizarTipoVehiculo(self, tipo: TipoVehiculo):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_tipovehiculo_por_id(?, ?, ?)}"
            cursor.execute(consulta, (tipo.GetIdTipo(), tipo.GetNombre(), tipo.GetDescripcion()))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl tipo de vehículo con ID {tipo.GetIdTipo()} no existe o no hubo cambios. No se actualizó información..")
            else:
                print(f"\nTipo de vehículo ID {tipo.GetIdTipo()} actualizado correctamente")

        except Exception as e:
            print(f"\nError al actualizar tipo de vehículo: {e}")

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def EliminarTipoVehiculo(self, id_tipo: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_tipovehiculo(?)}"
            cursor.execute(consulta, (id_tipo,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl tipo de vehículo con ID {id_tipo} no existe. No se eliminó información.")
            else:
                print(f"\nTipo de vehículo ID {id_tipo} eliminado correctamente")

        except Exception as e:
            print(f"\nError al eliminar tipo de vehículo:", e)

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
