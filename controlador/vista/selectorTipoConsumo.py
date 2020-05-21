from tkinter import *
import sys

sys.path.append("C:/Users/CHEZ/Documents/finalProgra/controlador")
#import controladorValida

class interfazConsumo():
	def __init__(self):
		
		self.miframe = Frame()
		self.botonRA = Button(text="Agua residencial").grid(column= 0, row=1)
		self.botonRE = Button(text="Elctricidad residencial").grid(column= 0, row=2)
		self.botonCA = Button(text="Agua comercial").grid(column= 0, row=3)
		self.botonCE = Button(text="Elctricidad comercial").grid(column= 0, row=4)
		
		
