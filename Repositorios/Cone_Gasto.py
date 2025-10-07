import pyodbc
from Entidades.Gasto import Gasto
from Repositorios.Conexion import Conexion

class Conexion_Gasto(Conexion):

    def CargarGastos(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_gastos()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay gastos registrados en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                g = Gasto()
                g.SetIdGasto(elemento[0])
                g.SetDescripcion(elemento[1])
                g.SetMonto(elemento[2])
                g.SetFecha(elemento[3])
                g.SetIdEmpleado(elemento[4])
                lista.append(g)

            return lista

        except Exception as e:
            print("\nError al cargar gastos:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    def InsertarGasto(self, gasto: Gasto):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_gasto(?, ?, ?, ?)}"
            cursor.execute(consulta, (
                gasto.GetDescripcion(),
                gasto.GetMonto(),
                gasto.GetFecha(),
                gasto.GetIdEmpleado()
            ))
            conexion.commit()
            print(f"\nGasto '{gasto.GetDescripcion()}' insertado correctamente.")

        except Exception as e:
            print("\nError al insertar gasto:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    def ActualizarGasto(self, gasto: Gasto):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_gasto(?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                gasto.GetIdGasto(),
                gasto.GetDescripcion(),
                gasto.GetMonto(),
                gasto.GetFecha(),
                gasto.GetIdEmpleado()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl gasto con ID {gasto.GetIdGasto()}no existe o no hubo cambios. No se actualizó información.")
            else:
                print(f"\nGasto ID {gasto.GetIdGasto()} actualizado correctamente.")

        except Exception as e:
            print("\nError al actualizar gasto:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    def EliminarGasto(self, id_gasto: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_gasto(?)}"
            cursor.execute(consulta, (id_gasto,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl gasto con ID {id_gasto} no existe. No se eliminó información.")
            else:
                print(f"\nGasto ID {id_gasto} eliminado correctamente.")

        except Exception as e:
            print("\nError al eliminar gasto:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
