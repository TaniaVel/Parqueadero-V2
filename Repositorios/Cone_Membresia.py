import pyodbc
from Entidades.Membresia import Membresia
from Repositorios.Conexion import Conexion

class Conexion_Membresia(Conexion):

    # -------------------- CARGAR MEMBRESÍAS --------------------
    def CargarMembresias(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_membresias()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay membresías registradas en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                m = Membresia()
                m.SetIdMembresia(elemento[0])
                m.SetIdCliente(elemento[1])
                m.SetFechaInicio(elemento[2])
                m.SetFechaFin(elemento[3])
                m.SetTipo(elemento[4])
                m.SetDescuento(elemento[5])
                m.SetEstado(elemento[6])
                lista.append(m)

            return lista

        except Exception as e:
            print("\nError al cargar membresías:", e)
            return []

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    # -------------------- INSERTAR MEMBRESÍA --------------------
    def InsertarMembresia(self, membresia: Membresia):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_membresia(?, ?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                membresia.GetIdCliente(),
                membresia.GetFechaInicio(),
                membresia.GetFechaFin(),
                membresia.GetTipo(),
                membresia.GetDescuento(),
                membresia.GetEstado()
            ))
            conexion.commit()
            print(f"\n Membresía para el cliente ID {membresia.GetIdCliente()} insertada correctamente.")

        except pyodbc.IntegrityError as e:
            print("\n Error de integridad al insertar membresía:", e)

        except Exception as e:
            print("\n Error al insertar membresía:", e)

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    # -------------------- ACTUALIZAR MEMBRESÍA --------------------
    def ActualizarMembresia(self, membresia: Membresia):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_membresia(?, ?, ?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                membresia.GetIdMembresia(),
                membresia.GetIdCliente(),
                membresia.GetFechaInicio(),
                membresia.GetFechaFin(),
                membresia.GetTipo(),
                membresia.GetDescuento(),
                membresia.GetEstado()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\n La membresía con ID {membresia.GetIdMembresia()} no existe o no hubo cambios. No se actualizó información.")
            else:
                print(f"\n Membresía con ID {membresia.GetIdMembresia()} actualizada correctamente.")

        except pyodbc.IntegrityError as e:
            print("\n Error de integridad al actualizar membresía:", e)

        except Exception as e:
            print("\n Error al actualizar membresía:", e)

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    # -------------------- ELIMINAR MEMBRESÍA --------------------
    def EliminarMembresia(self, id_membresia: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_membresia(?)}"
            cursor.execute(consulta, (id_membresia,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\n La membresía con ID {id_membresia} no existe. No se eliminó información.")
            else:
                print(f"\n Membresía con ID {id_membresia} eliminada correctamente.")

        except Exception as e:
            print("\n Error al eliminar membresía:", e)

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
