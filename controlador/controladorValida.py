import csv
import sys

sys.path.append("C:/Users/CHEZ/Documents/finalProgra/controlador/modelo")
sys.path.append("C:/Users/CHEZ/Documents/finalProgra/controlador/vista")

from selectorTipoConsumo import interfazConsumo 
from conexion import singleton  
from datoAgua import datoAgua

def validar(texto):
	
	textoAuxiliar = texto.get()	 
	
	if textoAuxiliar[-3,(len(textoAuxiliar)-1)] == "csv" or textoAuxiliar[-3,(len(textoAuxiliar)-1)] == "CSV" :
		leerArchivo(textoAuxiliar)
	else:
		texto.set("Archivo no valido")
		
def leerArchivo(rutaArchivo):
	with open (rutaArchivo) as archivoCSV : 
		lector = csv.reader(archivoCSV)
		for dato in lector:
			datoCarga = datoAgua(dato[0], dato[1])
			conector = singleton.Singleton(dato[0], dato[1])
			
def Valida(frame):
	
	frame.destroy()
	vista = interfazConsumo()
	frame = vista.miframe
	frame.pack()

		 
#leerArchivo('C:/Users/CHEZ/Desktop/ConsumoEnergiaComercial.csv')