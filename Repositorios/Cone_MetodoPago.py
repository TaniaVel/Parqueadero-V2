import pyodbc
from Entidades.MetodoPago import MetodoPago
from Repositorios.Conexion import Conexion


class Conexion_MetodoPago(Conexion):

    # -------------------- CARGAR MÉTODOS DE PAGO --------------------
    def CargarMetodos(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_metodo_pagos()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay métodos de pago registrados en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                m = MetodoPago()
                m.SetIdMetodo(elemento[0])
                m.SetNombre(elemento[1])
                m.SetDescripcion(elemento[2])
                lista.append(m)

            return lista

        except Exception as e:
            print("\nError al cargar métodos de pago:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- INSERTAR MÉTODO DE PAGO --------------------
    def InsertarMetodo(self, metodo: MetodoPago):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_metodo_pago(?, ?)}"
            cursor.execute(consulta, (
                metodo.GetNombre(),
                metodo.GetDescripcion()
            ))
            conexion.commit()
            print(f"\n Método de pago '{metodo.GetNombre()}' insertado correctamente.")

        except pyodbc.IntegrityError as e:
            print("\n Error de integridad (posible duplicado o restricción):", e)

        except Exception as e:
            print("\n Error al insertar método de pago:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- ACTUALIZAR MÉTODO DE PAGO --------------------
    def ActualizarMetodo(self, metodo: MetodoPago):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()

            # Verificar si el método existe antes de actualizar
            cursor.execute("SELECT COUNT(*) FROM MetodoPago WHERE id_metodo = ?", (metodo.GetIdMetodo(),))
            existe = cursor.fetchone()[0]

            if existe == 0:
                print(f"\n El método de pago con ID {metodo.GetIdMetodo()} no existe. No se puede actualizar.")
                return

            # Ejecutar actualización
            consulta = "{CALL proc_update_metodo_pago(?, ?, ?)}"
            cursor.execute(consulta, (
                metodo.GetIdMetodo(),
                metodo.GetNombre(),
                metodo.GetDescripcion()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\n No hubo cambios: los valores son iguales a los actuales para el método ID {metodo.GetIdMetodo()}.")
            else:
                print(f"\n Método de pago con ID {metodo.GetIdMetodo()} actualizado correctamente.")

        except pyodbc.IntegrityError as e:
            if "Duplicate entry" in str(e):
                print(f"\n Error: Ya existe un método de pago con el nombre '{metodo.GetNombre()}'.")
            else:
                print("\n Error de integridad al actualizar método de pago:", e)

        except Exception as e:
            print("\n Error general al actualizar método de pago:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- ELIMINAR MÉTODO DE PAGO --------------------
    def EliminarMetodo(self, id_metodo: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_metodo_pago(?)}"
            cursor.execute(consulta, (id_metodo,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\n El método de pago con ID {id_metodo} no existe. No se eliminó información.")
            else:
                print(f"\n Método de pago con ID {id_metodo} eliminado correctamente.")

        except Exception as e:
            print("\n Error al eliminar método de pago:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
