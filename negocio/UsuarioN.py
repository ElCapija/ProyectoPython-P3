
class usuarioN:

    #METODO PARA VALIDAR CUENTAS
    def validar_cuenta(self, numero_cuenta):

        try:
            conexion = Conexion().conectar()
            cursor = conexion.cursor() #Cursor es el objeto que ejecuta SQL

            cursor.execute(
                "SELECT 1 FROM Cuentas WHERE numero_cuenta = ?", # SELECT 1 = no importa el contenido real, solo interesa saber si existe fila
                (numero_cuenta,)
            )

            existe = cursor.fetchone() #Fetchone = toma una sola fila del resultado SQL

            if existe:
                return True, None
            
            return False, "Cuenta no existe" #no existe la cuenta


        except Exception as ex:
            return False, str(ex) #error del SQL

        finally:
            conexion.close()


