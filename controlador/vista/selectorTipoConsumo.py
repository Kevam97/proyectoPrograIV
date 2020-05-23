from tkinter import *
import sys

sys.path.append("C:/Users/CHEZ/Documents/finalProgra/controlador")
import controladorInsercion

class interfazConsumo():
	def __init__(self):
		
		self.miframe = Frame()
		self.botonRA = Button(self.miframe,text="Agua residencial", command= lambda:controladorInsercion.insertarDomesticoAgua()).grid(column= 0, row=1)
		self.botonRE = Button(self.miframe,text="Elctricidad residencial", command= lambda:controladorInsercion.insertarDomesticoLuz()).grid(column= 0, row=2)
		self.botonCA = Button(self.miframe,text="Agua comercial", command= lambda:controladorInsercion.insertarComercialAgua()).grid(column= 0, row=3)
		self.botonCE = Button(self.miframe,text="Elctricidad comercial", command= lambda:controladorInsercion.insertarComercialLuz()).grid(column= 0, row=4)
		
		
