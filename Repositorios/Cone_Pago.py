import pyodbc
from Entidades.Pago import Pago
from Repositorios.Conexion import Conexion

class Conexion_Pago(Conexion):

    def CargarPagos(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_pagos()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay pagos registrados en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                p = Pago()
                p.SetIdPago(elemento[0])
                p.SetIdRegistro(elemento[1])
                p.SetIdMetodo(elemento[2])
                p.SetMonto(elemento[3])
                p.SetFechaPago(str(elemento[4]))
                p.SetIdEmpleado(elemento[5])
                lista.append(p)

            return lista

        except Exception as e:
            print("\nError al cargar pagos:", e)
            return []

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def InsertarPago(self, pago: Pago):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_pago(?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                pago.GetIdRegistro(),
                pago.GetIdMetodo(),
                pago.GetMonto(),
                pago.GetFechaPago(),
                pago.GetIdEmpleado()
            ))
            conexion.commit()
            print(f"\nPago registrado correctamente con monto: {pago.GetMonto()}")

        except pyodbc.IntegrityError as e:
            print("\nError de integridad en la inserción del pago:", e)

        except Exception as e:
            print("\nError al insertar pago:", e)

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def ActualizarPago(self, pago: Pago):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_pago(?, ?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                pago.GetIdPago(),
                pago.GetIdRegistro(),
                pago.GetIdMetodo(),
                pago.GetMonto(),
                pago.GetFechaPago(),
                pago.GetIdEmpleado()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl pago con ID {pago.GetIdPago()} no existe o no hubo cambios. No se actualizó información.")
            else:
                print(f"\nPago con ID {pago.GetIdPago()} actualizado correctamente")

        except Exception as e:
            print(f"\nError al actualizar pago: {e}")

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def EliminarPago(self, id_pago: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_pago(?)}"
            cursor.execute(consulta, (id_pago,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl pago con ID {id_pago} no existe. No se eliminó información.")
            else:
                print(f"\nPago con ID {id_pago} eliminado correctamente")

        except Exception as e:
            print(f"\nError al eliminar pago:", e)

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
