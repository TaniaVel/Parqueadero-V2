import pyodbc
from Entidades.RolEmpleado import RolEmpleado
from Repositorios.Conexion import Conexion


class Conexion_RolEmpleado(Conexion):

    # -------------------- CARGAR ROLES --------------------
    def CargarRoles(self):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_rol_empleados()}"
            cursor.execute(consulta)

            filas = cursor.fetchall()
            if len(filas) == 0:
                print("\nNo hay roles registrados en la base de datos.")
                return []

            lista = []
            for elemento in filas:
                r = RolEmpleado()
                r.SetIdRol(elemento[0])
                r.SetNombre(elemento[1])
                r.SetDescripcion(elemento[2])
                lista.append(r)

            return lista

        except Exception as e:
            print("\nError al cargar roles:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    # -------------------- INSERTAR ROL --------------------
    def InsertarRol(self, rol: RolEmpleado):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_rol_empleado(?, ?)}"
            cursor.execute(consulta, (
                rol.GetNombre(),
                rol.GetDescripcion()
            ))
            conexion.commit()
            print(f"\nRol '{rol.GetNombre()}' insertado correctamente.")

        except pyodbc.IntegrityError as e:
            print("\nError de integridad (posible duplicado o restricción):", e)

        except Exception as e:
            print("\nError al insertar rol:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    # -------------------- ACTUALIZAR ROL --------------------


    def ActualizarRol(self, rol: RolEmpleado):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()

            # Verificar si el rol existe antes de actualizar
            cursor.execute("SELECT COUNT(*) FROM RolEmpleado WHERE id_rol = ?", (rol.GetIdRol(),))
            existe = cursor.fetchone()[0]

            if existe == 0:
                print(f"\El rol con ID {rol.GetIdRol()} no existe. No se puede actualizar.")
                return

            # Ejecutar actualización
            consulta = "{CALL proc_update_rol_empleado(?, ?, ?)}"
            cursor.execute(consulta, (
                rol.GetIdRol(),
                rol.GetNombre(),
                rol.GetDescripcion()
            ))
            conexion.commit()

            # Verificar si hubo cambios
            if cursor.rowcount == 0:
                print(f"\n No hubo cambios: los valores ingresados son iguales a los actuales para el rol ID {rol.GetIdRol()}.")
            else:
                print(f"\n Rol con ID {rol.GetIdRol()} actualizado correctamente.")

        # Evitar duplicados
        except pyodbc.IntegrityError as e:
            if "Duplicate entry" in str(e):
                print(f"\n Error: Ya existe un rol con el nombre '{rol.GetNombre()}'. Intente con otro nombre.")
            else:
                print("\n Error de integridad al actualizar el rol:", e)

        except Exception as e:
            print("\n Error general al actualizar rol:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    # -------------------- ELIMINAR ROL --------------------
    def EliminarRol(self, id_rol: int):
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_rol_empleado(?)}"
            cursor.execute(consulta, (id_rol,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\nEl rol con ID {id_rol} no existe. No se eliminó información.")
            else:
                print(f"\nRol con ID {id_rol} eliminado correctamente.")

        except Exception as e:
            print("\nError al eliminar rol:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
