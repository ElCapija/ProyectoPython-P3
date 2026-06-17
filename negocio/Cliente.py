class Cliente:

    #Constructor
    def __init__(self, identificacion, nombre):

        #PARAMETROS
        self.__identificacion = identificacion
        self.__nombre = nombre

    #GETTERS
    def get_identificacion(self):
        return self.__identificacion


    def get_nombre(self):
        return self.__nombre