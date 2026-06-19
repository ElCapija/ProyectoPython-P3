from datos.UsuarioD import UsuarioD
from negocio.Movimiento import Movimiento


class Cuenta:

    #Constructor
    def __init__(self, numero_cuenta, cliente):

        #PARAMETROS
        self.__numero_cuenta = numero_cuenta
        self.__cliente = cliente
        self.__usuarioD = UsuarioD()

    #GETTERS
    def get_numero_cuenta(self):
        return self.__numero_cuenta


    def get_cliente(self):
        return self.__cliente
    




    #METODOS DE LOGICA

    #METODO DEPOSITAR
    def depositar(self, codigo_cajero, monto): #recibe cual cajero y cual

        return self.__usuarioD.depositar( #se llama a capa de datos
            self.__numero_cuenta, #parametros
            codigo_cajero,
            monto
        )
    



    #METODO RETIRAR
    def retirar(self, codigo_cajero, monto):

        return self.__usuarioD.retirar(
            self.__numero_cuenta,
            codigo_cajero,
            monto
        )
    



    #METODO CONSULTAR SALDO
    def consultar_saldo(self):

        return self.__usuarioD.consultar_saldo(
            self.__numero_cuenta
        )




    #METODO HISTORIAL
    def historial_movimientos(self, fecha_inicio, fecha_fin):

        exito, datos = self.__usuarioD.historial_movimientos(
            self.__numero_cuenta,
            fecha_inicio,
            fecha_fin
        )

        if not exito:
            return False, datos

        movimientos = [] #crea lista vacia

        for fila in datos: #recorre cada fila SQL
            movimiento = Movimiento(*fila) # * desempaqueta la tupla que viene del SQL y la guarda como objeto con los valores internos de la clase Movimiento
            movimientos.append(movimiento) #con append lo guarda en la lista movimientos

        return True, movimientos #retorno final con la lista llena de objetos para mostrar en interfaz




    #METODO PAGAR SERVICIO
    def pagar_servicio(self, codigo_cajero, servicio, monto):

        return self.__usuarioD.pagar_servicio(self.__numero_cuenta, codigo_cajero, servicio, monto)
    



    #METODO COMPROBANTE

    def obtener_comprobante(self):

        ok, data = self.__usuarioD.obtener_comprobante(self.__numero_cuenta)

        if not ok:
            return False, data

        mov = Movimiento(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5],
            data[6],
            data[7]
        )

        return True, mov