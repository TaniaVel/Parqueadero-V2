import pyodbc
from Entidades.Multa import Multa
from Repositorios.Conexion import Conexion

class Conexion_Multa(Conexion):

    # -------------------- CARGAR MULTAS --------------------
    def CargarMultas(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_multas()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay multas registradas en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                m = Multa()
                m.SetIdMulta(elemento[0])
                m.SetIdRegistro(elemento[1])
                m.SetMotivo(elemento[2])
                m.SetValor(float(elemento[3]))
                m.SetFecha(elemento[4].strftime("%Y-%m-%d %H:%M:%S") if elemento[4] else None)
                lista.append(m)

            return lista

        except Exception as e:
            print("\nError al cargar multas:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- INSERTAR MULTA --------------------
    def InsertarMulta(self, multa: Multa):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_multa(?, ?, ?, ?)}"
            cursor.execute(consulta, (
                multa.GetIdRegistro(),
                multa.GetMotivo(),
                multa.GetValor(),
                multa.GetFecha()
            ))
            conexion.commit()
            print(f"\n✅ Multa '{multa.GetMotivo()}' insertada correctamente.")

        except pyodbc.IntegrityError as e:
            print("\n⚠ Error de integridad al insertar multa:", e)

        except Exception as e:
            print("\n❌ Error al insertar multa:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- ACTUALIZAR MULTA --------------------
    def ActualizarMulta(self, multa: Multa):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_multa(?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                multa.GetIdMulta(),
                multa.GetIdRegistro(),
                multa.GetMotivo(),
                multa.GetValor(),
                multa.GetFecha()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\n La multa con ID {multa.GetIdMulta()} no existe o no hubo cambios. No se actualizó información.")
            else:
                print(f"\n Multa ID {multa.GetIdMulta()} actualizada correctamente.")

        except Exception as e:
            print("\n Error al actualizar multa:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- ELIMINAR MULTA --------------------
    def EliminarMulta(self, id_multa: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_multa(?)}"
            cursor.execute(consulta, (id_multa,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\n La multa con ID {id_multa} no existe. No se eliminó información.")
            else:
                print(f"\n Multa ID {id_multa} eliminada correctamente.")

        except Exception as e:
            print("\n Error al eliminar multa:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
