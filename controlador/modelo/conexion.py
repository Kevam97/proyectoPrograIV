import sqlite3
class conexion:
    
    _instance = None
    def __init__(self):
        self.listaInsertar = None
    def foo(self):
        print(id(self))
     #esta clase lleva la logica de la conexion
    def insertar(self, nombreTabla):
        print(self.listaInsertar)
        
    def leerDatos(self,listaInsertar):
        self.listaInsertar = listaInsertar        
        
class singleton():
    def __init__(self):
        self.cls = conexion
    def Singleton(self):
        if (not self.cls._instance):
            self.cls._instance = self.cls()
        return (self.cls)