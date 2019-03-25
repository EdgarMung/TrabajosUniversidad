from tkinter import *
import tkinter
from PIL import Image
from PIL import ImageTk

def Proceso():
	pass

# Inicio de la Ventana
ventana = tkinter.Tk()
ventana.title("Integrales Complejas")
Entradas = tkinter.Frame(ventana)
Salida = tkinter.Frame(ventana)
Entradas.pack(side=LEFT)
Salida.pack(side=LEFT)

#Etiquetas para definir las Entradas
tkinter.Label(Entradas,text=" Entradas",pady=5 ,font="bold 20").grid(row = 0 ,column = 0)
tkinter.Label(Entradas,text="    Radio (r): " ,pady=3).grid(row = 1 ,column = 0)
tkinter.Label(Entradas,text="Numero Z0: ",pady=3 ).grid(row = 2 ,column = 0)
tkinter.Label(Entradas,text="Numero n: ",pady=3 ).grid(row = 3 ,column = 0)
tkinter.Label(Entradas,text="\t\t\t" ).grid(row = 4 ,column = 0,columnspan=2)

#Campos Para meter los datos de la entrada
campo_Radio = tkinter.Entry(Entradas)
campo_Radio.grid(row = 1 ,column = 1)
campo_Radio.insert(0,"0")

campo_Z0 = tkinter.Entry(Entradas)
campo_Z0.grid(row = 2 ,column = 1)
campo_Z0.insert(0,"0")

campo_n = tkinter.Entry(Entradas)
campo_n.grid(row = 3,column = 1)
campo_n.insert(0,"0")

#Boton para Ingresar los datos proporcionados 
tkinter.Button(Entradas, text = " Ingresar Datos ", command = Proceso).grid(row = 4 ,column = 0,columnspan=2)


#Etiquetas para definir las Salidas
tkinter.Label(Salida,text="Salida",pady=5 ,font="bold 20").grid(row = 0 ,column = 0)
ventana.mainloop()