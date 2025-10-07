import pyodbc
from Entidades.Factura import Factura
from Repositorios.Conexion import Conexion

class Conexion_Factura(Conexion):

    # -------------------- CARGAR FACTURAS --------------------
    def CargarFacturas(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_facturas()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay facturas registradas en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                f = Factura()
                f.SetIdFactura(elemento[0])
                f.SetIdPago(elemento[1])
                f.SetNumeroFactura(elemento[2])
                f.SetFechaEmision(str(elemento[3]))
                f.SetTotal(float(elemento[4]))
                lista.append(f)

            return lista

        except Exception as e:
            print("\nError al cargar facturas:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- INSERTAR FACTURA --------------------
    def InsertarFactura(self, factura: Factura):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_factura(?, ?, ?, ?)}"
            cursor.execute(consulta, (
                factura.GetIdPago(),
                factura.GetNumeroFactura(),
                factura.GetFechaEmision(),
                factura.GetTotal()
            ))
            conexion.commit()
            print(f"\n Factura '{factura.GetNumeroFactura()}' insertada correctamente.")

        except pyodbc.IntegrityError as e:
            print("\n Error de integridad (posible duplicado o restricción):", e)

        except Exception as e:
            print("\n Error al insertar factura:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- ACTUALIZAR FACTURA --------------------
    def ActualizarFactura(self, factura: Factura):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_factura(?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                factura.GetIdFactura(),
                factura.GetIdPago(),
                factura.GetNumeroFactura(),
                factura.GetFechaEmision(),
                factura.GetTotal()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nLa factura con ID {factura.GetIdFactura()} no existe o no hubo cambios. No se actualizó información.")
            else:
                print(f"\nFactura con ID {factura.GetIdFactura()} actualizada correctamente.")

        except pyodbc.IntegrityError as e:
            if "Duplicate entry" in str(e):
                print(f"\n Error: Ya existe una factura con el número '{factura.GetNumeroFactura()}'.")
            else:
                print("\n Error de integridad al actualizar factura:", e)

        except Exception as e:
            print("\n Error general al actualizar factura:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    # -------------------- ELIMINAR FACTURA --------------------
    def EliminarFactura(self, id_factura: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_factura(?)}"
            cursor.execute(consulta, (id_factura,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nLa factura con ID {id_factura} no existe. No se eliminó información.")
            else:
                print(f"\n Factura con ID {id_factura} eliminada correctamente.")

        except Exception as e:
            print("\nError al eliminar factura:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
