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


    def _existe_membresia_activa(self, id_cliente: int, tipo: str, id_membresia_actual=None) -> bool:
    
        #Verifica si el cliente ya tiene una membresía activa del mismo tipo.
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()

            consulta = """
                SELECT id_membresia 
                FROM Membresia
                WHERE id_cliente = ?
                  AND tipo = ?
                  AND estado = 'Activa'
            """

            cursor.execute(consulta, (id_cliente, tipo))
            resultado = cursor.fetchone()

            if not resultado:
                return False

            # Si estamos actualizando, ignorar si el encontrado es el mismo registro
            if id_membresia_actual and resultado[0] == id_membresia_actual:
                return False

            return True

        except Exception as e:
            print("Error validando duplicado:", e)
            return False

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()



    # -------------------- VALIDAR DATOS DE MEMBRESÍA --------------------
    def _validar_membresia(self, membresia: Membresia, modo="insertar"):
        """
        Realiza validaciones lógicas antes de insertar o actualizar una membresía.
        """

        # Validar fechas
        if membresia.GetFechaFin() <= membresia.GetFechaInicio():
            raise ValueError("La fecha de fin debe ser mayor que la fecha de inicio.")

        # Validar descuento
        if membresia.GetDescuento() is None or membresia.GetDescuento() < 0:
            raise ValueError("El descuento debe ser un valor mayor o igual a 0.")

        # Validar tipo válido
        tipos_validos = ["Mensual", "Trimestral", "Anual"]
        if membresia.GetTipo() not in tipos_validos:
            raise ValueError(f"Tipo inválido. Permitidos: {tipos_validos}")

        # Validar estado
        estados_validos = ["Activa", "Vencida"]
        if membresia.GetEstado() not in estados_validos:
            raise ValueError(f"Estado inválido. Permitidos: {estados_validos}")

        # ------------ VALIDACIÓN NUEVA: evitar duplicados activos ----------
        if membresia.GetEstado() == "Activa":
            existe = self._existe_membresia_activa(
                membresia.GetIdCliente(),
                membresia.GetTipo(),
                membresia.GetIdMembresia() if modo == "actualizar" else None
            )

            if existe:
                raise ValueError(
                    f"El cliente {membresia.GetIdCliente()} ya tiene una membresía activa de tipo {membresia.GetTipo()}."
                )

    
    # -------------------- INSERTAR MEMBRESÍA --------------------
    def InsertarMembresia(self, membresia: Membresia):
        conexion = None
        cursor = None
        try:
            # VALIDACIÓN ANTES DE INSERTAR
            self._validar_membresia(membresia)

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

        except ValueError as e:
            print("\n Error de validación:", e)

        except pyodbc.IntegrityError as e:
            print("\n Error de integridad al insertar membresía:", e)

        except Exception as e:
            print("\n Error al insertar membresía:", e)


    # -------------------- ACTUALIZAR MEMBRESÍA --------------------
    def ActualizarMembresia(self, membresia: Membresia):
        conexion = None
        cursor = None
        try:
            # VALIDACIÓN ANTES DE ACTUALIZAR
            self._validar_membresia(membresia)

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
                print(f"\n La membresía con ID {membresia.GetIdMembresia()} no existe o no hubo cambios.")
            else:
                print(f"\n Membresía con ID {membresia.GetIdMembresia()} actualizada correctamente.")

        except ValueError as e:
            print("\n Error de validación:", e)

        except pyodbc.IntegrityError as e:
            print("\n Error de integridad al actualizar membresía:", e)

        except Exception as e:
            print("\n Error al actualizar membresía:", e)


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
