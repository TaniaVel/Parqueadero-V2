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


    def _validar_metodo(self, metodo: MetodoPago, modo="insertar"):
        #Valida datos del método de pago antes de insertar o actualizar.
      
        # Validar nombre
        nombre = metodo.GetNombre()
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre del método de pago es obligatorio.")

        if nombre.isnumeric():
            raise ValueError("El nombre del método de pago no puede ser solo números.")

        if len(nombre) >5:
            raise ValueError("El nombre del método de pago no debe superar 5 caracteres.")

        descripcion = metodo.GetDescripcion()
        if descripcion and descripcion.strip() == "":
            raise ValueError("La descripción no debe contener solo espacios.")

        if descripcion and len(descripcion) > 100:
            raise ValueError("La descripción supera el límite permitido (100 caracteres).")

        # Validar duplicado al insertar
        if modo == "insertar":
            if self._existe_nombre(nombre):
                raise ValueError(f"Ya existe un método de pago con el nombre '{nombre}'.")

        # Validar duplicado al actualizar
        if modo == "actualizar":
            if self._existe_nombre(nombre, metodo.GetIdMetodo()):
                raise ValueError(f"Ya existe otro método de pago con el nombre '{nombre}'.")
        
    def _existe_nombre(self, nombre: str, id_excluir=None) -> bool:
        conexion = None
        cursor = None
        try:
            conexion = self.get_conexion()
            cursor = conexion.cursor()

            consulta = "SELECT id_metodo FROM MetodoPago WHERE nombre = ?"
            cursor.execute(consulta, (nombre,))
            resultado = cursor.fetchone()

            if resultado:
                if id_excluir and resultado[0] == id_excluir:
                    return False  # Es el mismo registro
                return True

            return False

        except Exception as e:
            print("Error en validación de nombre duplicado:", e)
            return False

        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()


    # -------------------- INSERTAR MÉTODO DE PAGO --------------------
    def InsertarMetodo(self, metodo: MetodoPago):
        conexion = None
        cursor = None
        try:
            # Validaciones
            self._validar_metodo(metodo, modo="insertar")

            conexion = self.get_conexion()
            cursor = conexion.cursor()

            consulta = "{CALL proc_insert_metodo_pago(?, ?)}"
            cursor.execute(consulta, (
                metodo.GetNombre(),
                metodo.GetDescripcion()
            ))
            conexion.commit()

            print(f"\n Método de pago '{metodo.GetNombre()}' insertado correctamente.")

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
            # Validaciones
            self._validar_metodo(metodo, modo="actualizar")

            conexion = self.get_conexion()
            cursor = conexion.cursor()

            consulta = "{CALL proc_update_metodo_pago(?, ?, ?)}"
            cursor.execute(consulta, (
                metodo.GetIdMetodo(),
                metodo.GetNombre(),
                metodo.GetDescripcion()
            ))
            conexion.commit()

            if cursor.rowcount == 0:
                print(f"\n No hubo cambios para el método de pago ID {metodo.GetIdMetodo()}.")
            else:
                print(f"\n Método de pago ID {metodo.GetIdMetodo()} actualizado correctamente.")

        except Exception as e:
            print("\n Error al actualizar método de pago:", e)

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
