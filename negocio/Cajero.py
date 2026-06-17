class Cajero:
    
    #Constructor
    def __init__(self, codigo, ubicacion): 

        #PARAMETROS
        self.__codigo = codigo #atributos privados con __ para encapsulacion
        self.__ubicacion = ubicacion

    #GETTERS
    def get_codigo(self): #getter codigo
        return self.__codigo #permite obtener el codigo


    def get_ubicacion(self):
        return self.__ubicacion
    
    