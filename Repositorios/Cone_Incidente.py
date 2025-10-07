import pyodbc
from Entidades.Incidente import Incidente
from Repositorios.Conexion import Conexion

class Conexion_Incidente(Conexion):

    # -------------------- CARGAR INCIDENTES --------------------
    def CargarIncidentes(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_incidentes()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay incidentes registrados en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                i = Incidente()
                i.SetIdIncidente(elemento[0])
                i.SetIdRegistro(elemento[1])
                i.SetDescripcion(elemento[2])
                i.SetFecha(elemento[3])
                i.SetIdEmpleado(elemento[4])
                lista.append(i)

            return lista

        except Exception as e:
            print("\nError al cargar incidentes:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- INSERTAR INCIDENTE --------------------
    def InsertarIncidente(self, incidente: Incidente):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_incidente(?, ?, ?, ?)}"
            cursor.execute(consulta, (
                incidente.GetIdRegistro(),
                incidente.GetDescripcion(),
                incidente.GetFecha(),
                incidente.GetIdEmpleado()
            ))
            conexion.commit()
            print(f"\n✅ Incidente registrado correctamente para el registro ID {incidente.GetIdRegistro()}.")

        except pyodbc.IntegrityError as e:
            print("\n Error de integridad (posible referencia inexistente):", e)

        except Exception as e:
            print("\n Error al insertar incidente:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- ACTUALIZAR INCIDENTE --------------------
    def ActualizarIncidente(self, incidente: Incidente):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_incidente(?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                incidente.GetIdIncidente(),
                incidente.GetIdRegistro(),
                incidente.GetDescripcion(),
                incidente.GetFecha(),
                incidente.GetIdEmpleado()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl incidente con ID {incidente.GetIdIncidente()} no existe o no hubo cambios. No se actualizó información.")
            else:
                print(f"\n Incidente ID {incidente.GetIdIncidente()} actualizado correctamente.")

        except Exception as e:
            print("\n Error al actualizar incidente:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- ELIMINAR INCIDENTE --------------------
    def EliminarIncidente(self, id_incidente: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_incidente(?)}"
            cursor.execute(consulta, (id_incidente,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl incidente con ID {id_incidente} no existe. No se eliminó información.")
            else:
                print(f"\n Incidente ID {id_incidente} eliminado correctamente.")

        except Exception as e:
            print("\n Error al eliminar incidente:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
