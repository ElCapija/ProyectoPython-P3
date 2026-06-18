class Movimiento:

    def __init__(
        self,
        id_movimiento,
        nombre_cliente,
        numero_cuenta,
        codigo_cajero,
        tipo,
        servicio,
        monto,
        saldo_anterior,
        saldo_resultante,
        fecha
    ):

        #Parametros
        self.__id_movimiento = id_movimiento
        self.__nombre_cliente = nombre_cliente
        self.__numero_cuenta = numero_cuenta
        self.__codigo_cajero = codigo_cajero
        self.__tipo = tipo
        self.__servicio = servicio
        self.__monto = monto
        self.__saldo_anterior = saldo_anterior
        self.__saldo_resultante = saldo_resultante
        self.__fecha = fecha


    # GETTERS
    def get_id_movimiento(self):
        return self.__id_movimiento


    def get_nombre_cliente(self):
        return self.__nombre_cliente


    def get_numero_cuenta(self):
        return self.__numero_cuenta


    def get_codigo_cajero(self):
        return self.__codigo_cajero


    def get_tipo(self):
        return self.__tipo


    def get_servicio(self):
        return self.__servicio


    def get_monto(self):
        return self.__monto


    def get_saldo_anterior(self):
        return self.__saldo_anterior


    def get_saldo_resultante(self):
        return self.__saldo_resultante


    def get_fecha(self):
        return self.__fecha