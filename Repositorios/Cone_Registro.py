import pyodbc
from Entidades.Entradasalida  import Entradasalida
from Repositorios.Conexion import Conexion


class Conexion_Registro(Conexion):

    # -------------------- CARGAR REGISTROS --------------------
    def CargarRegistros(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_registros()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay registros de entrada/salida en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                r = Entradasalida()
                r.SetIdRegistro(elemento[0])
                r.SetIdVehiculo(elemento[1])
                r.SetIdEmpleado(elemento[2])
                r.SetFechaEntrada(elemento[3])
                r.SetFechaSalida(elemento[4])
                r.SetEspacio(elemento[5])
                lista.append(r)

            return lista

        except Exception as e:
            print("\nError al cargar registros:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    # -------------------- INSERTAR REGISTRO --------------------
    def InsertarRegistro(self, registro: Entradasalida):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_registro(?, ?, ?, ?)}"
            cursor.execute(consulta, (
                registro.GetIdVehiculo(),
                registro.GetIdEmpleado(),
                registro.GetFechaEntrada(),
                registro.GetEspacio()
            ))
            conexion.commit()
            print(f"\nRegistro de entrada creado correctamente para vehículo ID {registro.GetIdVehiculo()}.")

        except pyodbc.IntegrityError as e:
            print("\nError de integridad (posible clave foránea o duplicado):", e)

        except Exception as e:
            print("\nError al insertar registro:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    # -------------------- ACTUALIZAR REGISTRO (SALIDA) --------------------
    def ActualizarSalida(self, registro: Entradasalida):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_salida(?, ?)}"
            cursor.execute(consulta, (
                registro.GetIdRegistro(),
                registro.GetFechaSalida()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl registro con ID {registro.GetIdRegistro()} no existe o no hubo cambios. No se actualizó información.")
            else:
                print(f"\nSalida registrada correctamente para el registro ID {registro.GetIdRegistro()}.")

        except Exception as e:
            print("\nError al actualizar salida:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    # -------------------- ELIMINAR REGISTRO --------------------
    def EliminarRegistro(self, id_registro: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_registro(?)}"
            cursor.execute(consulta, (id_registro,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl registro con ID {id_registro} no existe. No se eliminó información.")
            else:
                print(f"\nRegistro ID {id_registro} eliminado correctamente.")

        except Exception as e:
            print("\nError al eliminar registro:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
