import pyodbc
from Entidades.Tarifa import Tarifa
from Repositorios.Conexion import Conexion

class Conexion_Tarifa(Conexion):

    # -------------------- CARGAR TARIFAS --------------------
    def CargarTarifas(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_tarifas()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay tarifas registradas en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                t = Tarifa()
                t.SetIdTarifa(elemento[0])
                t.SetIdTipo(elemento[1])
                t.SetTipoTarifa(elemento[2])
                t.SetValor(elemento[3])
                lista.append(t)

            return lista

        except Exception as e:
            print("\nError al cargar tarifas:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- INSERTAR TARIFA --------------------
    def InsertarTarifa(self, tarifa: Tarifa):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_tarifa(?, ?, ?)}"
            cursor.execute(consulta, (
                tarifa.GetIdTipo(),
                tarifa.GetTipoTarifa(),
                tarifa.GetValor()
            ))
            conexion.commit()
            print(f"\n Tarifa insertada correctamente.")

        except pyodbc.IntegrityError as e:
            print("\n Error de integridad (posible duplicado o restricción):", e)

        except Exception as e:
            print("\n Error al insertar tarifa:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- ACTUALIZAR TARIFA --------------------
    def ActualizarTarifa(self, tarifa: Tarifa):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_tarifa(?, ?, ?, ?)}"
            cursor.execute(consulta, (
                tarifa.GetIdTarifa(),
                tarifa.GetIdTipo(),
                tarifa.GetTipoTarifa(),
                tarifa.GetValor()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\n La tarifa con ID {tarifa.GetIdTarifa()} no existe o no hubo cambios. No se actualizó información..")
            else:
                print(f"\n Tarifa con ID {tarifa.GetIdTarifa()} actualizada correctamente.")

        except pyodbc.IntegrityError as e:
            print("\n Error de integridad al actualizar tarifa:", e)

        except Exception as e:
            print("\n Error general al actualizar tarifa:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- ELIMINAR TARIFA --------------------
    def EliminarTarifa(self, id_tarifa: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_tarifa(?)}"
            cursor.execute(consulta, (id_tarifa,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\n La tarifa con ID {id_tarifa} no existe. No se eliminó información.")
            else:
                print(f"\n Tarifa con ID {id_tarifa} eliminada correctamente.")

        except Exception as e:
            print("\n Error al eliminar tarifa:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
