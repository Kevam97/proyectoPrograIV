from tkinter import *
import sys

sys.path.append("C:/Users/CHEZ/Documents/finalProgra/controlador")
#import controladorValida

class interfazConsumo():
	def __init__(self):
		
		self.miframe = Frame()
		self.botonRA = Button(self.miframe,text="Agua residencial").grid(column= 0, row=1)
		self.botonRE = Button(self.miframe,text="Elctricidad residencial").grid(column= 0, row=2)
		self.botonCA = Button(self.miframe,text="Agua comercial").grid(column= 0, row=3)
		self.botonCE = Button(self.miframe,text="Elctricidad comercial").grid(column= 0, row=4)
		
		
