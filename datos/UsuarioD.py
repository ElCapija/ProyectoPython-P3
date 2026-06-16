from datos.Conexion import Conexion


class UsuarioD:

    #METODO DEPOSITAR
    def depositar(self, numero_cuenta, codigo_cajero, monto):

        try:

            conexion = Conexion().conectar()
            cursor = conexion.cursor() 

            cursor.execute(
                "EXEC SP_Depositar ?, ?, ?", #ejecuta el SP, se usa ? como placeholder para evitar errores de formato
                (numero_cuenta, codigo_cajero, monto)
            )

            conexion.commit() #Guarda el deposito
            return True, None

        except Exception as ex: #captura errores
            return False, str(ex).split(']')[-1].strip() #muestra el error claro

        finally: #finally se ejecuta siempre, aunque haya errores

            conexion.close() #cierra conexion



    #METODO RETIRAR
    def retirar(self, numero_cuenta, codigo_cajero, monto):

        try:

            conexion = Conexion().conectar()

            cursor = conexion.cursor()

            cursor.execute(
                "EXEC SP_Retirar ?, ?, ?",
                (numero_cuenta, codigo_cajero, monto)
            )

            conexion.commit()
            return True, None

        except Exception as ex:
            return False, str(ex).split(']')[-1].strip()

        finally:

            conexion.close()       



    #METODO CONSULTAR
    def consultar_saldo(self, numero_cuenta):

        try:
            conexion = Conexion().conectar()
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
            conexion.close() 



    #METODO HISTORIAL
    def historial_movimientos(self, numero_cuenta, fecha_inicio, fecha_fin):

        try:
            conexion = Conexion().conectar()
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
            conexion.close()