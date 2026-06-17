class Movimiento:

    #Constructor
    def __init__(
        self,
        id_movimiento,
        codigo_cajero,
        tipo,
        monto,
        saldo_anterior,
        saldo_resultante,
        fecha
    ):

        #PARAMETROS
        self.__id_movimiento = id_movimiento
        self.__codigo_cajero = codigo_cajero
        self.__tipo = tipo
        self.__monto = monto
        self.__saldo_anterior = saldo_anterior
        self.__saldo_resultante = saldo_resultante
        self.__fecha = fecha

    #GETTERS
    def get_id_movimiento(self):
        return self.__id_movimiento


    def get_codigo_cajero(self):
        return self.__codigo_cajero


    def get_tipo(self):
        return self.__tipo


    def get_monto(self):
        return self.__monto


    def get_saldo_anterior(self):
        return self.__saldo_anterior


    def get_saldo_resultante(self):
        return self.__saldo_resultante


    def get_fecha(self):
        return self.__fecha