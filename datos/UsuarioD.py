from datos.Conexion import Conexion


class UsuarioD:

    #METODO DEPOSITAR
    def depositar(self, numero_cuenta, codigo_cajero, monto):

        conexion = None #se inicializa la conexion en none para evitar errores de conexion fallida al querer cerrar

        try:

            conexion = Conexion.conectar()
            cursor = conexion.cursor() 

            cursor.execute(
                "EXEC SP_Depositar ?, ?, ?", #ejecuta el SP, se usa ? como placeholder para evitar errores de formato
                (numero_cuenta, codigo_cajero, monto)
            )

            conexion.commit() #Guarda el deposito
            return True, None

        except Exception as ex:

            mensaje = str(ex)

            if "Error" in mensaje:

                mensaje = "Ocurrió un error al procesar la operación"

            return False, mensaje

        finally: #finally se ejecuta siempre, aunque haya errores

            if conexion: #if por si no se habia conectado al inicio que no se ejecute el cerrar
                conexion.close() #cierra conexion




    #METODO RETIRAR
    def retirar(self, numero_cuenta, codigo_cajero, monto):

        conexion = None

        try:

            conexion = Conexion.conectar()

            cursor = conexion.cursor()

            cursor.execute(
                "EXEC SP_Retirar ?, ?, ?",
                (numero_cuenta, codigo_cajero, monto)
            )

            conexion.commit()
            return True, None

        except Exception as ex:

            mensaje = str(ex)

            if "Fondos insuficientes" in mensaje:

                mensaje = "Fondos insuficientes"

            elif "Error" in mensaje:

                mensaje = "Ocurrió un error al procesar la operación"

            return False, mensaje

        finally:

            if conexion:
                conexion.close()
      




    #METODO CONSULTAR
    def consultar_saldo(self, numero_cuenta):

        conexion = None

        try:
            conexion = Conexion.conectar()
            cursor = conexion.cursor()

            cursor.execute(
                "SELECT saldo FROM Cuentas WHERE numero_cuenta = ?",
                (numero_cuenta,)
            )

            resultado = cursor.fetchone()

            if resultado:
                return True, resultado[0]  # saldo, posicion[0]
            else:
                return False, "Cuenta no existe"

        except Exception as ex:
            return False, str(ex)

        finally:

            if conexion:
                conexion.close()

    #METODO HISTORIAL MOVIMIENTOS
    def historial_movimientos(self, numero_cuenta, fecha_inicio, fecha_fin):

        conexion = None

        try:
            conexion = Conexion.conectar()
            cursor = conexion.cursor()

            cursor.execute(
                "EXEC SP_HistorialMovimientos ?, ?, ?", 
                (numero_cuenta, fecha_inicio, fecha_fin)
            )

            datos = cursor.fetchall() #obtiene todas las filas

            return True, datos

        except Exception as ex:
            return False, str(ex)

        finally:

            if conexion:
                conexion.close()

    #METODO PAGAR SERVICIO
    def pagar_servicio(self, numero_cuenta, codigo_cajero, servicio, monto):

        conexion = None

        try:

            conexion = Conexion.conectar()
            cursor = conexion.cursor()

            cursor.execute(
                "EXEC SP_PagarServicio ?, ?, ?, ?",
                (numero_cuenta, codigo_cajero, servicio, monto)
            )

            conexion.commit()
            return True, None

        except Exception as ex:

            mensaje = str(ex)

            if "Fondos insuficientes" in mensaje:

                mensaje = "Fondos insuficientes"

            elif "Error" in mensaje:

                mensaje = "Ocurrió un error al procesar la operación"

            return False, mensaje

        finally:

            if conexion:
                conexion.close()




    #METODO HISTORIAL MOVIMIENTOS
    def obtener_comprobante(self, numero_cuenta):

        conexion = None

        try:

            conexion = Conexion().conectar()

            cursor = conexion.cursor()

            cursor.execute(

                "EXEC SP_ObtenerComprobante ?",

                (numero_cuenta,)

            )

            resultado = cursor.fetchone()

            return True, resultado


        except Exception as ex:

            return False, str(ex)


        finally:

            if conexion:

                conexion.close()