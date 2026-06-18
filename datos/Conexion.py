import pyodbc

class Conexion:

    usuario_actual = None
    contraseña_actual = None

    @staticmethod
    def conectar(usuario=None, contraseña=None):

        if usuario:
            Conexion.usuario_actual = usuario

        if contraseña:
            Conexion.contraseña_actual = contraseña

        try:

            conn = pyodbc.connect(
                "DRIVER={ODBC Driver 18 for SQL Server};"
                "SERVER=CARLOSPC\\SQLEXPRESS01;"
                "DATABASE=Cajeros;"
                f"UID={Conexion.usuario_actual};"
                f"PWD={Conexion.contraseña_actual};"
                "TrustServerCertificate=yes;"
            )

            return conn

        except Exception as ex:

            print(ex)
            return None