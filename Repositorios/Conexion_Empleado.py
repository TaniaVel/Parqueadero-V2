import pyodbc
from Entidades.Empleado import Empleado
from Repositorios.Conexion import Conexion

class Conexion_Empleado(Conexion):

    def CargarEmpleados(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_empleados()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay empleados registrados en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                e = Empleado()
                e.SetIdEmpleado(elemento[0])
                e.SetNombre(elemento[1])
                e.SetDocumento(elemento[2])
                e.SetTelefono(elemento[3])
                e.SetCorreo(elemento[4])
                e.SetIdRol(elemento[5])
                lista.append(e)

            return lista

        except Exception as e:
            print("\nError al cargar empleados:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    def InsertarEmpleado(self, empleado: Empleado):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_empleado(?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                empleado.GetNombre(),
                empleado.GetDocumento(),
                empleado.GetTelefono(),
                empleado.GetCorreo(),
                empleado.GetIdRol()
            ))
            conexion.commit()
            print(f"\nEmpleado '{empleado.GetNombre()}' insertado correctamente.")

        except pyodbc.IntegrityError as e:
            if "Duplicate entry" in str(e):
                print(f"\nError: El documento '{empleado.GetDocumento()}' ya existe en la base de datos.")
            else:
                print("\nError de integridad:", e)

        except Exception as e:
            print("\nError al insertar empleado:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    def ActualizarEmpleado(self, empleado: Empleado):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()

            # Consultar datos actuales
            cursor.execute("SELECT nombre, documento, telefono, correo, id_rol FROM Empleado WHERE id_empleado = ?", 
                           (empleado.GetIdEmpleado(),))
            datos_actuales = cursor.fetchone()

            if not datos_actuales:
                print(f"\nEl empleado con ID {empleado.GetIdEmpleado()} no existe.")
                return

            nombre_act, doc_act, tel_act, correo_act, rol_act = datos_actuales

            # Si los datos son iguales, no hacer nada
            if (empleado.GetNombre() == nombre_act and
                empleado.GetDocumento() == doc_act and
                empleado.GetTelefono() == tel_act and
                empleado.GetCorreo() == correo_act and
                empleado.GetIdRol() == rol_act):
                print(f"\nNo se realizaron cambios: los datos del empleado ID {empleado.GetIdEmpleado()} son los mismos.")
                return

            # Verificar duplicado de documento
            cursor.execute("SELECT COUNT(*) FROM Empleado WHERE documento = ? AND id_empleado <> ?", 
                           (empleado.GetDocumento(), empleado.GetIdEmpleado()))
            if cursor.fetchone()[0] > 0:
                print(f"\nError: El documento '{empleado.GetDocumento()}' ya está asignado a otro empleado.")
                return

            
            consulta = "{CALL proc_update_empleado_por_id(?, ?, ?, ?, ?, ?)}"
            cursor.execute(consulta, (
                empleado.GetIdEmpleado(),
                empleado.GetNombre(),
                empleado.GetDocumento(),
                empleado.GetTelefono(),
                empleado.GetCorreo(),
                empleado.GetIdRol()
            ))
            conexion.commit()
            print(f"\nEmpleado ID {empleado.GetIdEmpleado()} actualizado correctamente.")

        except Exception as e:
            print("\nError al actualizar empleado:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    def EliminarEmpleado(self, id_empleado: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_empleado(?)}"
            cursor.execute(consulta, (id_empleado,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl empleado con ID {id_empleado} no existe. No se eliminó información.")
            else:
                print(f"\nEmpleado ID {id_empleado} eliminado correctamente.")

        except Exception as e:
            print("\nError al eliminar empleado:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
