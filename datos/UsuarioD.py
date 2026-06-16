from datos.Conexion import Conexion


class UsuarioD:

    #METODO DEPOSITAR
    def depositar(self, numero_cuenta, codigo_cajero, monto):

        try:

            conexion = Conexion().conectar()

            cursor = conexion.cursor() #Cursor es el objeto que ejecuta SQL

            cursor.execute(
                "EXEC SP_Depositar ?, ?, ?",
                numero_cuenta,
                codigo_cajero,
                monto
            )

            conexion.commit() #Guarda el deposito

            return True

        except Exception as ex: #captura errores

            print(ex)

            return False

        finally: #finally se ejecuta siempre, aunque haya errores

            conexion.close() #cierra conexion



    #METODO RETIRAR
    def retirar(self, numero_cuenta, codigo_cajero, monto):

        try:

            conexion = Conexion().conectar()

            cursor = conexion.cursor()

            cursor.execute(
                "EXEC SP_Retirar ?, ?, ?",
                numero_cuenta,
                codigo_cajero,
                monto
            )

            conexion.commit()

            return True

        except Exception as ex:

            print(ex)

            return False

        finally:

            conexion.close()        