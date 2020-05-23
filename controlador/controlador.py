#from modelo import conexion
from .vista.apertura import Apertura
from tkinter import filedialog 

dirArchivo = None

def Valida(frame,texto):
	
	frame.forget()
	vista = Apertura(texto)
	frame = vista.miframe
	frame.pack()
	
def BuscarArchivo(texto): 
	global dirArchivo
	filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV","*.csv*"),("all files", "*.*"))) 
	texto.set(filename)
	dirArchivo = filename 
	print(dirArchivo)  