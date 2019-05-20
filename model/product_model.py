import psycopg2

class Product():
    def __init__(self, id, name, value):
        self.__id = id
        self.__name = name
        self.__value = value

    def atualizar(self, id, name, value):
        self.__id = id
        self.__name = name
        self.__value = value
        return self
    
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value
