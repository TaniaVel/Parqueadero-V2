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

    def _validar_promocion(self, promocion: Promocion, modo="insertar"):
        
        #Valida los datos de una promoción antes de insertar o actualizar.

        # ---- Validar nombre ----
        nombre = promocion.GetNombre()
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre de la promoción es obligatorio.")
        
        if nombre.isnumeric():
            raise ValueError("El nombre de la promoción no puede ser solo números.")

        if len(nombre) > 100:
            raise ValueError("El nombre de la promoción no debe superar 100 caracteres.")

        # ---- Validar descripción ----
        descripcion = promocion.GetDescripcion()
        if descripcion and descripcion.strip() == "":
            raise ValueError("La descripción no puede contener solo espacios.")

        if descripcion and len(descripcion) > 200:
            raise ValueError("La descripción supera el límite de 200 caracteres.")

        # ---- Validar descuento ----
        descuento = promocion.GetDescuento()
        if descuento is None:
            raise ValueError("El descuento es obligatorio.")

        if descuento <= 0 or descuento > 100:
            raise ValueError("El descuento debe ser mayor a 0 y menor o igual a 100.")

        # ---- Validar fechas ----
        fecha_inicio = promocion.GetFechaInicio()
        fecha_fin = promocion.GetFechaFin()

        if fecha_inicio >= fecha_fin:
            raise ValueError("La fecha de inicio debe ser menor que la fecha de fin.")

        # ---- Validación de duplicado ----
        if modo == "insertar":
            if self._existe_nombre(nombre):
                raise ValueError(f"Ya existe una promoción con el nombre '{nombre}'.")

        if modo == "actualizar":
            if self._existe_nombre(nombre, promocion.GetIdPromocion()):
                raise ValueError(f"Ya existe otra promoción con el nombre '{nombre}'.")

    def _existe_nombre(self, nombre: str, id_excluir=None) -> bool:
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()

            consulta = "SELECT id_promocion FROM Promocion WHERE nombre = ?"
            cursor.execute(consulta, (nombre,))
            resultado = cursor.fetchone()

            if resultado:
                if id_excluir and resultado[0] == id_excluir:
                    return False
                return True
            
            return False

        except Exception as e:
            print("Error validando nombre duplicado:", e)
            return False

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()



    # -------------------- INSERTAR PROMOCIÓN --------------------
    def InsertarPromocion(self, promocion: Promocion):
        conexion = None
        cursor = None
        try:
            # Validaciones antes de insertar
            self._validar_promocion(promocion, modo="insertar")

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

        except ValueError as ve:
            #  Error de validación (datos incorrectos)
            print("\n Validación fallida al insertar promoción:", ve)

        except pyodbc.IntegrityError as e:
            print("\nError de integridad (duplicado o restricción):", e)

        except Exception as e:
            print("\nError general al insertar promoción:", e)

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


# -------------------- ACTUALIZAR PROMOCIÓN --------------------
    def ActualizarPromocion(self, promocion: Promocion):
        conexion = None
        cursor = None
        try:
            # 🔍 Validaciones antes de actualizar
            self._validar_promocion(promocion, modo="actualizar")

            conexion = self.get_conexion()
            cursor = conexion.cursor()

            # 🔎 Verificar si existe antes de actualizar
            cursor.execute("SELECT COUNT(*) FROM Promocion WHERE id_promocion = ?", 
                           (promocion.GetIdPromocion(),))
            existe = cursor.fetchone()[0]

            if existe == 0:
                print(f"\n La promoción con ID {promocion.GetIdPromocion()} no existe. No se puede actualizar.")
                return

            # Ejecutar actualización
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
                print(f"\n No hubo cambios. Los valores enviados son iguales a los actuales.")
            else:
                print(f"\n Promoción ID {promocion.GetIdPromocion()} actualizada correctamente.")

        except ValueError as ve:
            print("\n Validación fallida al actualizar promoción:", ve)

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
