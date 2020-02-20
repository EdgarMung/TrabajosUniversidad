import tkinter as tk
from PIL import Image,ImageTk
from AFN import AFN
from tkinter import ttk
from tkinter import messagebox

# Funciones que ayudan a realizar las funciones **************************************************************
def CreacionAFNSimple(Diccionario,Lista,Entrada,root):
    print(Diccionario)
    caract = Entrada.get()
    if caract != "":
        if Diccionario.get(caract) == None:
            Diccionario[caract] = AFN(simbolo=caract)
            Lista.delete(0,tk.END)
            Elementos = list(Diccionario.keys())
            Lista.insert(tk.END,*Elementos)
            messagebox.showinfo(message="La Creacion del AFN '"+ caract +"' fue Exitosa", title="Confirmacion",parent = root)
        else:
            messagebox.showerror(message="El caracter ingresado ya fue ocupado. Por favor, ocupar otro.",title="Entrada Vacia",parent = root)
        
        Entrada.delete(0, tk.END)
    else:
        messagebox.showerror(message="No se ha detectado ningun caracter, por favor ingrese alguno.",title="Entrada Vacia",parent = root)
    print(Diccionario)

def CreacionUnion(Diccionario,Lista_a,Lista_b,root):
    print(Diccionario)

    Elemento_a = Lista_a.get()
    Elemento_b = Lista_b.get()

    if Elemento_a != "" and Elemento_b != "": 
        if Elemento_a != Elemento_b:
            Objeto_A = Diccionario.get(Elemento_a)
            Objeto_B = Diccionario.get(Elemento_b)

            Objeto_A.union(Objeto_B)

            KeyAux = "("+Elemento_a + "|" +Elemento_b+")" 
            ObjetoAux = Objeto_A

            Diccionario.pop(Elemento_a)
            Diccionario.pop(Elemento_b)
            Diccionario[KeyAux] = ObjetoAux
            messagebox.showinfo(message="La Union entre '"+ Elemento_a +" y "+ Elemento_b+"' fue Exitosa", title="Confirmacion",parent = root)
        else:
            messagebox.showerror(message="Se ha seleccionado el mismo AFN para la union, por favor revise.",title="Mismo AFN",parent = root)
    else:
        messagebox.showerror(message="No se ha seleccionado uno de los dos AFN, por favor revise.",title="Lista Vacia",parent = root)
    
    Lista_a.set("")
    Lista_b.set("")
    Elementos = list(Diccionario.keys())
    Lista_a ["values"] = Elementos
    Lista_b ["values"] = Elementos
    print(Diccionario)

def CreacionConcatenacion(Diccionario,Lista_a,Lista_b,root):
    print(Diccionario)
    Elemento_a = Lista_a.get()
    Elemento_b = Lista_b.get()

    if Elemento_a != "" and Elemento_b != "": 
        if Elemento_a != Elemento_b:
            Objeto_A = Diccionario.get(Elemento_a)
            Objeto_B = Diccionario.get(Elemento_b)

            Objeto_A.concatenacion(Objeto_B)

            KeyAux = "("+Elemento_a + "°" +Elemento_b+")" 
            ObjetoAux = Objeto_A

            Diccionario.pop(Elemento_a)
            Diccionario.pop(Elemento_b)
            Diccionario[KeyAux] = ObjetoAux
            messagebox.showinfo(message="La Concatenacion entre '"+ Elemento_a +" y "+ Elemento_b+"' fue Exitosa", title="Confirmacion",parent = root)
        else:
            messagebox.showerror(message="Se ha seleccionado el mismo AFN para la concatenación, por favor revise.",title="Mismo AFN",parent = root)
    else:
        messagebox.showerror(message="No se ha seleccionado uno de los dos AFN, por favor revise.",title="Lista Vacia",parent = root)
    
    Lista_a.set("")
    Lista_b.set("")
    Elementos = list(Diccionario.keys())
    Lista_a ["values"] = Elementos
    Lista_b ["values"] = Elementos
    print(Diccionario)

def CreacionCerraduraPositiva(Diccionario,Lista,root):
    print(Diccionario)
    AFN = Lista.get()
    if AFN != "":
        Objeto = Diccionario.get(AFN)

        Objeto.cerradura_positiva()

        KeyAux = "("+AFN + ")+"
        ObjetoAux = Objeto

        Diccionario.pop(AFN)
        Diccionario[KeyAux] = ObjetoAux
        messagebox.showinfo(message="La Cerradura Positiva a '"+ AFN +"' fue Exitosa", title="Confirmacion",parent=root)
    else:
        messagebox.showerror(message="No se ha seleccionado algun AFN, por favor revise.",title="Lista Vacia",parent = root)
    Lista.set("")
    Elementos = list(Diccionario.keys())
    Lista["values"] = Elementos
    print(Diccionario)

def CreacionCerraduraKleene(Diccionario,Lista,root):
    print(Diccionario)
    AFN = Lista.get()
    if AFN != "":
        Objeto = Diccionario.get(AFN)

        Objeto.cerradura_kleene()

        KeyAux = "("+AFN + ")*"
        ObjetoAux = Objeto

        Diccionario.pop(AFN)
        Diccionario[KeyAux] = ObjetoAux
        messagebox.showinfo(message="La Cerradura de Kleene a '"+ AFN +"' fue Exitosa", title="Confirmacion",parent= root)
    else:
        messagebox.showerror(message="No se ha seleccionado algun AFN, por favor revise.",title="Lista Vacia",parent = root)
    Lista.set("")
    Elementos = list(Diccionario.keys())
    Lista["values"] = Elementos
    print(Diccionario)
    
def CreacionCerraduraOpcional(Diccionario,Lista,root):
    print(Diccionario)
    AFN = Lista.get()
    if AFN != "":
        Objeto = Diccionario.get(AFN)

        Objeto.interrogacion()

        KeyAux = "("+AFN + ")?"
        ObjetoAux = Objeto

        Diccionario.pop(AFN)
        Diccionario[KeyAux] = ObjetoAux
        messagebox.showinfo(message="La Cerradura Opcional a '"+ AFN +"' fue Exitosa", title="Confirmacion",parent = root)
    else:
        messagebox.showerror(message="No se ha seleccionado algun AFN, por favor revise.",title="Lista Vacia",parent = root)
    Lista.set("")
    Elementos = list(Diccionario.keys())
    Lista["values"] = Elementos
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
            Entrada.place(x = 330, y = 50 )

            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionAFNSimple(self.DiccionarioObjetos,lista,Entrada,ventana)).place( x = 420, y = 46)
            lista = tk.Listbox(ventana)
            

            lista.insert(tk.END,*Elementos)
            lista.place(x = 50, y = 80)
            
            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 220 , y = 100)

        if tipo_ventana == "Union":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/Union.jpeg")
            aux = aux.resize((320, 170), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)
            
            tk.Label(ventana, text="Union entre: ").place(x = 50, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_a.place(x = 135, y = 50)
            
            AFN_b = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_b.place(x = 275, y = 50)

            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionUnion(self.DiccionarioObjetos,AFN_a,AFN_b,ventana)).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 90 , y = 75)

        if tipo_ventana == "Concatenacion":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/Concatenacion.jpeg")
            aux = aux.resize((350, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)
            
            tk.Label(ventana, text="Concatenacion entre: ").place(x = 25, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 12)
            AFN_a.place(x = 160, y = 50)
            
            AFN_b = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 12)
            AFN_b.place(x = 290, y = 50)

            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionConcatenacion(self.DiccionarioObjetos,AFN_a,AFN_b,ventana)).place( x = 410, y = 46)

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
            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionCerraduraPositiva(self.DiccionarioObjetos,AFN_a,ventana)).place( x = 410, y = 46)

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
            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionCerraduraKleene(self.DiccionarioObjetos,AFN_a,ventana)).place( x = 410, y = 46)

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
            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: CreacionCerraduraOpcional(self.DiccionarioObjetos,AFN_a,ventana)).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 70 , y = 100)

        tk.Button(ventana, text="Cerrar" , fg="red", command = ventana.destroy).place(x = 225, y = 250)

    def Mostrar(self):
        Elementos = list(self.DiccionarioObjetos.keys())

        for i in Elementos:
            Objeto = self.DiccionarioObjetos[i]
            Objeto.imprimir_transiciones()
