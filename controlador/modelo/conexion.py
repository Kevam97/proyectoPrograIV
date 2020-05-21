import sqlite3
class conexion:
    
    def __init__(self, fechaInsertar, consumoInsertar):
        self.fechaInsertar = fechaInsertar
        self.consumoInsertar = consumoInsertar
        self._instance = None
    def foo(self):
        return id(self)
     #esta clase lleva la logica de la conexion
    def printer(self):
     	print("aqui")
     	
    def insertar(self,datosInsertar):
    	pass

class singleton():
    def __init__(self):
        self.cls = conexion
    def Singleton(self, fechaInsertar, consumoInsertar):
        if (not self.cls._instance):
            self.cls._instance = self.cls(fechaInsertar, consumoInsertar)
        return (self.cls)