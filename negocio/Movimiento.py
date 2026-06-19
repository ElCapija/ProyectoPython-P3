from abc import ABC, abstractmethod
 

class Movimiento(ABC): #ABC= abstraccion en python
 
    def __init__(
        self,
        id_movimiento,
        codigo_cajero,
        tipo,
        servicio,
        monto,
        saldo_anterior,
        saldo_resultante,
        fecha
    ):
        #Atributos 
        self._Movimiento__id_movimiento = id_movimiento
        self._Movimiento__codigo_cajero = codigo_cajero
        self._Movimiento__tipo = tipo
        self._Movimiento__servicio = servicio
        self._Movimiento__monto = monto
        self._Movimiento__saldo_anterior = saldo_anterior
        self._Movimiento__saldo_resultante = saldo_resultante
        self._Movimiento__fecha = fecha
 
    # GETTERS 
    def get_id_movimiento(self):
        return self._Movimiento__id_movimiento
 
    def get_codigo_cajero(self):
        return self._Movimiento__codigo_cajero
 
    def get_tipo(self):
        return self._Movimiento__tipo
 
    def get_servicio(self):
        return self._Movimiento__servicio
 
    def get_monto(self):
        return self._Movimiento__monto
 
    def get_saldo_anterior(self):
        return self._Movimiento__saldo_anterior
 
    def get_saldo_resultante(self):
        return self._Movimiento__saldo_resultante
 
    def get_fecha(self):
        return self._Movimiento__fecha
 
    
    @abstractmethod
    def descripcion(self):
        pass
 
 
 
class Deposito(Movimiento):
 
    def descripcion(self):
        return f"Depósito de ₡{self.get_monto():,.2f}"
 
 
class Retiro(Movimiento):
 
    def descripcion(self):
        return f"Retiro de ₡{self.get_monto():,.2f}"
 
 
class Consulta(Movimiento):
 
    def descripcion(self):
        return "Consulta de saldo"
 
 
class PagoServicio(Movimiento):
 
    def descripcion(self):
        return f"Pago de {self.get_servicio()}: ₡{self.get_monto():,.2f}"
 
 

def crear_movimiento(id_movimiento, codigo_cajero, tipo, servicio,
                      monto, saldo_anterior, saldo_resultante, fecha):
 
    tipo_normalizado = (tipo or "").strip().lower()
 
    if "deposit" in tipo_normalizado:
        clase = Deposito
    elif "retir" in tipo_normalizado:
        clase = Retiro
    elif "consulta" in tipo_normalizado:
        clase = Consulta
    elif "pago" in tipo_normalizado:
        clase = PagoServicio
    else:
        # Si no reconoce el tipo, usa Deposito como genérico para no romper nada
        clase = Deposito
 
    return clase(
        id_movimiento,
        codigo_cajero,
        tipo,
        servicio,
        monto,
        saldo_anterior,
        saldo_resultante,
        fecha
    )