import tkinter as tk
from PIL import Image,ImageTk
from AFN import AFN
from tkinter import ttk
from tkinter import messagebox

# Funciones que ayudan a realizar las funciones **************************************************************
def CreacionAFNSimple(Diccionario,Lista,Entrada):
    print(Diccionario)
    caract = Entrada.get()
    Diccionario[caract] = AFN(simbolo=caract)
    Lista.delete(0,tk.END)
    Elementos = list(Diccionario.keys())
    Lista.insert(tk.END,*Elementos)
    messagebox.showinfo(message="La Creacion del AFN '"+ caract +"' fue Exitosa", title="Confirmacion")
    Entrada.delete(0, tk.END)
    print(Diccionario)

def CreacionUnion(Diccionario,Elemento_a,Elemento_b):
    print(Diccionario)
    Objeto_A = Diccionario.get(Elemento_a)
    Objeto_B = Diccionario.get(Elemento_b)

    Objeto_A.union(Objeto_B)

    KeyAux = "("+Elemento_a + "|" +Elemento_b+")" 
    ObjetoAux = Objeto_A

    Diccionario.pop(Elemento_a)
    Diccionario.pop(Elemento_b)
    Diccionario[KeyAux] = ObjetoAux
    messagebox.showinfo(message="La Union entre '"+ Elemento_a +" y "+ Elemento_b+"' fue Exitosa", title="Confirmacion")
    print(Diccionario)

def CreacionConcatenacion(Diccionario,Elemento_a,Elemento_b):
    print(Diccionario)
    Objeto_A = Diccionario.get(Elemento_a)
    Objeto_B = Diccionario.get(Elemento_b)

    Objeto_A.concatenacion(Objeto_B)

    KeyAux = "("+Elemento_a + "°" +Elemento_b+")" 
    ObjetoAux = Objeto_A

    Diccionario.pop(Elemento_a)
    Diccionario.pop(Elemento_b)
    Diccionario[KeyAux] = ObjetoAux
    messagebox.showinfo(message="La Concatenacion entre '"+ Elemento_a +" y "+ Elemento_b+"' fue Exitosa", title="Confirmacion")
    print(Diccionario)

def CreacionCerraduraPositiva(Diccionario,AFN):
    print(Diccionario)
    Objeto = Diccionario.get(AFN)

    Objeto.cerradura_positiva()

    KeyAux = "("+AFN + ")+"
    ObjetoAux = Objeto

    Diccionario.pop(AFN)
    Diccionario[KeyAux] = ObjetoAux
    messagebox.showinfo(message="La Cerradura Positiva a '"+ AFN +"' fue Exitosa", title="Confirmacion")
    print(Diccionario)

def CreacionCerraduraKleene(Diccionario,AFN):
    print(Diccionario)
    Objeto = Diccionario.get(AFN)

    Objeto.cerradura_kleene()

    KeyAux = "("+AFN + ")*"
    ObjetoAux = Objeto

    Diccionario.pop(AFN)
    Diccionario[KeyAux] = ObjetoAux
    messagebox.showinfo(message="La Cerradura de Kleene a '"+ AFN +"' fue Exitosa", title="Confirmacion")
    print(Diccionario)
    
def CreacionCerraduraOpcional(Diccionario,AFN):
    print(Diccionario)
    Objeto = Diccionario.get(AFN)

    Objeto.interrogacion()

    KeyAux = "("+AFN + ")?"
    ObjetoAux = Objeto

    Diccionario.pop(AFN)
    Diccionario[KeyAux] = ObjetoAux
    messagebox.showinfo(message="La Cerradura Opcional a '"+ AFN +"' fue Exitosa", title="Confirmacion")
    print(Diccionario)



# Clase para crear la pantalla **********************************************************************************
class Crear_Ventanas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.DiccionarioObjetos = {}
        self.master.geometry("400x550")
        self.master.title("Compiladores")
        self.pack()

    def create_widgets(self):

        tk.Button(self, text="AFN Basico", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("AFN Simple",self.master)).pack()
        tk.Button(self, text="Union", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Union",self.master)).pack()
        tk.Button(self, text="Concatenacion", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold" ,command = lambda: self.create_second_window("Concatenacion",self.master)).pack()
        tk.Button(self, text="Cerradura Positiva", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold" ,command = lambda: self.create_second_window("Cerradura+",self.master)).pack()
        tk.Button(self, text="Cerradura Kleene", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Cerradura*",self.master)).pack()
        tk.Button(self, text="Opcional", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Opcional",self.master)).pack()
        tk.Button(self, text="ImprimirTransiciones", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.Mostrar()).pack()
        self.quit = tk.Button(self, text="Cerrar" , fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_second_window(self,tipo_ventana,root):
        ventana = tk.Toplevel(root)
        ventana.title("Operación "+tipo_ventana)
        ventana.geometry("500x300")

        if tipo_ventana == "AFN Simple":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/AFNSimple.jpeg")
            aux = aux.resize((250, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)
            
            tk.Label(ventana, text="Por favor, Ingrese el caracter del AFN Simple: ").place(x = 50, y = 50)
            Entrada = tk.Entry(ventana,width = 10)
            Entrada.place(x = 300, y = 50 )

            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionAFNSimple(self.DiccionarioObjetos,lista,Entrada)).place( x = 380, y = 46)
            lista = tk.Listbox(ventana)
            

            lista.insert(tk.END,*Elementos)
            lista.place(x = 50, y = 80)
            
            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 200 , y = 100)

        if tipo_ventana == "Union":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/Union.jpeg")
            aux = aux.resize((320, 170), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)
            
            tk.Label(ventana, text="Union entre: ").place(x = 50, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_a.place(x = 150, y = 50)
            
            AFN_b = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_b.place(x = 280, y = 50)

            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionUnion(self.DiccionarioObjetos,AFN_a.get(),AFN_b.get())).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 90 , y = 75)

        if tipo_ventana == "Concatenacion":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/Concatenacion.jpeg")
            aux = aux.resize((350, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)
            
            tk.Label(ventana, text="Concatenacion entre: ").place(x = 25, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_a.place(x = 150, y = 50)
            
            AFN_b = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_b.place(x = 280, y = 50)

            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionConcatenacion(self.DiccionarioObjetos,AFN_a.get(),AFN_b.get())).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 70 , y = 120)

        if tipo_ventana == "Cerradura+":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/Cerradura+.jpeg")
            aux = aux.resize((350, 125), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)

            tk.Label(ventana, text="Cerradura Positiva a: ").place(x = 100, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_a.place(x = 250, y = 50)
            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionCerraduraPositiva(self.DiccionarioObjetos,AFN_a.get())).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 70 , y = 100)

        if tipo_ventana == "Cerradura*":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/Cerradura*.jpeg")
            aux = aux.resize((350, 125), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)

            tk.Label(ventana, text="Cerradura de Kleene a: ").place(x = 100, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_a.place(x = 250, y = 50)
            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionCerraduraKleene(self.DiccionarioObjetos,AFN_a.get())).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 70 , y = 100)

        if tipo_ventana == "Opcional":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/Opcional.jpeg")
            aux = aux.resize((350, 125), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)

            tk.Label(ventana, text="Cerradura Opcional a: ").place(x = 100, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_a.place(x = 250, y = 50)
            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionCerraduraOpcional(self.DiccionarioObjetos,AFN_a.get())).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 70 , y = 100)

        tk.Button(ventana, text="Cerrar" , fg="red", command = ventana.destroy).place(x = 225, y = 250)

    def Mostrar(self):
        Elementos = list(self.DiccionarioObjetos.keys())

        for i in Elementos:
            Objeto = self.DiccionarioObjetos[i]
            Objeto.imprimir_transiciones()
