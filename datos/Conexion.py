import pyodbc

class Conexion:

    def conectar(self):

        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=CARLOSPC\\SQLEXPRESS01;"
            "DATABASE=Cajeros;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )

        return conexion