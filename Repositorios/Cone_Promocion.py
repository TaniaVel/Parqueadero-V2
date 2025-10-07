import pyodbc
from Entidades.Promocion import Promocion
from Repositorios.Conexion import Conexion

class Conexion_Promocion(Conexion):

    # -------------------- CARGAR PROMOCIONES --------------------
    def CargarPromociones(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_promociones()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay promociones registradas en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                p = Promocion()
                p.SetIdPromocion(elemento[0])
                p.SetNombre(elemento[1])
                p.SetDescripcion(elemento[2])
                p.SetDescuento(elemento[3])
                p.SetFechaInicio(str(elemento[4]))
                p.SetFechaFin(str(elemento[5]))
                lista.append(p)

            return lista

        except Exception as e:
            print("\nError al cargar promociones:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    # -------------------- INSERTAR PROMOCIÓN --------------------
    def InsertarPromocion(self, promocion: Promocion):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_promocion(?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                promocion.GetNombre(),
                promocion.GetDescripcion(),
                promocion.GetDescuento(),
                promocion.GetFechaInicio(),
                promocion.GetFechaFin()
            ))
            conexion.commit()
            print(f"\n Promoción '{promocion.GetNombre()}' insertada correctamente.")

        except pyodbc.IntegrityError as e:
            print("\nError de integridad (posible duplicado o restricción):", e)

        except Exception as e:
            print("\n Error al insertar promoción:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    # -------------------- ACTUALIZAR PROMOCIÓN --------------------
    def ActualizarPromocion(self, promocion: Promocion):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()

            # Verificar si la promoción existe antes de actualizar
            cursor.execute("SELECT COUNT(*) FROM Promocion WHERE id_promocion = ?", (promocion.GetIdPromocion(),))
            existe = cursor.fetchone()[0]

            if existe == 0:
                print(f"\n La promoción con ID {promocion.GetIdPromocion()} no existe. No se puede actualizar.")
                return

            consulta = "{CALL proc_update_promocion(?, ?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                promocion.GetIdPromocion(),
                promocion.GetNombre(),
                promocion.GetDescripcion(),
                promocion.GetDescuento(),
                promocion.GetFechaInicio(),
                promocion.GetFechaFin()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\n No hubo cambios: los valores son iguales a los actuales para la promoción ID {promocion.GetIdPromocion()}.")
            else:
                print(f"\n Promoción con ID {promocion.GetIdPromocion()} actualizada correctamente.")

        except pyodbc.IntegrityError as e:
            print("\n Error de integridad al actualizar promoción:", e)

        except Exception as e:
            print("\n Error general al actualizar promoción:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    # -------------------- ELIMINAR PROMOCIÓN --------------------
    def EliminarPromocion(self, id_promocion: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_promocion(?)}"
            cursor.execute(consulta, (id_promocion,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\n La promoción con ID {id_promocion} no existe. No se eliminó información.")
            else:
                print(f"\n Promoción con ID {id_promocion} eliminada correctamente.")

        except Exception as e:
            print("\n Error al eliminar promoción:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
