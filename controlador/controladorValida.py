import csv
import sys
from puente import conector
sys.path.append("C:/Users/CHEZ/Documents/finalProgra/controlador/modelo")
sys.path.append("C:/Users/CHEZ/Documents/finalProgra/controlador/vista")

from selectorTipoConsumo import interfazConsumo 
from conexion import singleton  

def validar(texto):
	
	textoAuxiliar = texto.get()	 
	
	if textoAuxiliar[-3:(len(textoAuxiliar))] == "csv" or textoAuxiliar[-3:(len(textoAuxiliar))] == "CSV" :
		leerArchivo(textoAuxiliar)
	else:
		texto.set("Archivo no valido")
		
def leerArchivo(rutaArchivo):
	listaDatos = []
	with open (rutaArchivo) as archivoCSV : 
		lector = csv.reader(archivoCSV)
		for dato in lector:
			datoCarga = (dato[0], dato[1])
			listaDatos.append(datoCarga)
	archivoCSV.close()
	conector.leerDatos(conector,listaDatos)
	#conector.foo(conector)
	print(type(conector),"1")
			
def Valida(frame):
	
	frame.destroy()
	vista = interfazConsumo()
	frame = vista.miframe
	frame.pack()

		 
#leerArchivo('C:/Users/CHEZ/Desktop/ConsumoEnergiaComercial.csv')