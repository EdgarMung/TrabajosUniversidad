import tkinter as tk
from PIL import Image,ImageTk
from AFN import AFN
from tkinter import ttk
from tkinter import messagebox

# Funciones que ayudan a realizar las funciones **************************************************************
def ChecarToken(estado,estados,tokens):
    indice = estados.index(estado)

    return tokens[indice] 

def BuscarTransicion(caracter,transiciones,estado_Actual):
    transicionesDelEstado = transiciones.get(estado_Actual)

    for i in transicionesDelEstado:
        if caracter == i[0]:
            return i[1]
    
    return -1

def PertenceAlfabeto(caracter,alfabeto):
    for i in alfabeto:
        if caracter == i:
            return True
    
    return False

def AlgoritmoLex(cadena,Lista,AFD):
    estados = AFD.estados
    tokens = AFD.tokens
    Salida = []
    transiciones = AFD.transiciones
    alfabeto = AFD.alfabeto
    Lista.delete(0,tk.END)
    TamañoCadena = len(cadena)
    estado_Actual = 0

    if TamañoCadena == 0:
        token = ChecarToken(estado_Actual,estados,tokens)
        if token > -1:
            Salida.append(" "+" -> "+str(token))
    else:
        cadenaAux = ""
        for caracter in cadena:
            if PertenceAlfabeto(caracter,alfabeto):
                estado_Actual = BuscarTransicion(caracter,transiciones,estado_Actual)
                if estado_Actual > -1:
                    cadenaAux+= caracter
                    token = ChecarToken(estado_Actual,estados,tokens)
                    if token > -1:
                        Salida.append(cadenaAux+" -> "+str(token))
                        cadenaAux = ""
                else:
                    estado_Actual = 0
                    cadenaAux = ""
            else:
                cadenaAux = ""
                estado_Actual = 0
        
    Lista.insert(tk.END,*Salida)

def ObtencionTablaAFD(AFD,Lista):
    Aux = []
    token = 10
    for i in AFD.finales:
        if i == 1:
            AFD.tokens.append(token)
            token += 10
        else:
            AFD.tokens.append(-1)

    Elementos = list(AFD.transiciones.keys())

    Aux.append("Transiciones del AFD")
    for i in Elementos:
        auxTransicion = AFD.transiciones.get(i)
        Aux.append("    Estado " + str(i) + ": " +str(auxTransicion))
        
    #cadena = "     |" 
    #for i in AFD.alfabeto:
    #    cadena+= " "+i
    #cadena+=" | Aceptación"
    #Aux.append(cadena)
    #Elementos = list(AFD.transiciones.keys())
    #cadena = " ->"
    #for estado in AFD.estados:
    #    cadena+= str(estado) + "|"
    #    for caracter in AFD.alfabeto:
    #        for i in Elementos:
    #            auxTransicion = AFD.transiciones.get(i)
    #            for j in range(0,len(auxTransicion)):
    #                if auxTransicion[j][0] == caracter: 
    #                    cadena+=" "+str(auxTransicion[j][1])
    #                else:
    #                    cadena+=" -"
    #        cadena+=" |"        
    #        cadena+= str(AFD.tokens[AFD.estados.index(estado)])
    #        Aux.append(cadena)
    #        cadena = "    "
    Aux.append("")
    Aux.append("Estados y tokens")
    for i in range(0,len(AFD.estados)):
        Aux.append("    "+str(AFD.estados[i])+ " -> "+str(AFD.tokens[i]))
        
    Lista.insert(tk.END,*Aux)

def CreacionAFNSimple(Diccionario,Lista,Entrada,root):
    print(Diccionario)
    caract = Entrada.get()
    if caract != "":
        if Diccionario.get(caract) == None:
            Diccionario[caract] = AFN(simbolo=caract)
        else:
            llave = caract + " "
            Diccionario[llave] = AFN(simbolo=caract)

        Lista.delete(0,tk.END)
        Elementos = list(Diccionario.keys())
        Lista.insert(tk.END,*Elementos)
        messagebox.showinfo(message="La Creacion del AFN '"+ caract +"' fue Exitosa", title="Confirmacion",parent = root)  
        
        Entrada.delete(0, tk.END)
    else:
        messagebox.showerror(message="No se ha detectado ningun caracter, por favor ingrese alguno.",title="Entrada Vacia",parent = root)
    print(Diccionario)

def CreacionUnion(Diccionario,Lista_a,Lista_b,root):
    print(Diccionario)

    Elemento_a = Lista_a.get()
    Elemento_b = Lista_b.get()
    if Elemento_a != "" and Elemento_b != "": 
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

def CrearUnionEspecial(Diccionario):
    listaObjetos = []
    Elementos = list(Diccionario.keys())

    ObjetoUnico = Diccionario.get(Elementos[0])
    llave = Elementos.pop(0)

    for i in Elementos:
        listaObjetos.append(Diccionario.get(i))
        Diccionario.pop(i)

    ObjetoUnico.union_especial(listaObjetos)
    NuevaLlave = "Union_Especial"

    Diccionario.pop(llave)

    Diccionario[NuevaLlave] = ObjetoUnico

    messagebox.showinfo(message="La Union especial entre los AFN fue Exitosa", title="Confirmacion")

# Clase para crear la pantalla **********************************************************************************
class Crear_Ventanas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.DiccionarioObjetos = {}
        self.AFD = ""
        self.master.geometry("400x700")
        self.master.title("Compiladores")
        self.pack()

    def create_widgets(self):

        tk.Button(self, text="AFN Basico", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("AFN Simple",self.master)).pack()
        tk.Button(self, text="Union", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Union",self.master)).pack()
        tk.Button(self, text="Concatenacion", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold" ,command = lambda: self.create_second_window("Concatenacion",self.master)).pack()
        tk.Button(self, text="Cerradura Positiva", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold" ,command = lambda: self.create_second_window("Cerradura+",self.master)).pack()
        tk.Button(self, text="Cerradura Kleene", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Cerradura*",self.master)).pack()
        tk.Button(self, text="Opcional", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Opcional",self.master)).pack()
        tk.Button(self, text="Realizar Union Especial", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: CrearUnionEspecial(self.DiccionarioObjetos)).pack()
        tk.Button(self, text="ImprimirTransiciones", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Mostrar",self.master)).pack()
        tk.Button(self, text="Convertir AFN  a AFD", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Analizador",self.master)).pack()
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

        if tipo_ventana == "Mostrar":
            Elementos = list(self.DiccionarioObjetos.keys())
            AuxTexto = []

            for i in Elementos:
                cadenaAux = "AFN: " + i
                AuxTexto.append(cadenaAux)
                for key in range(len(list(self.DiccionarioObjetos[i].estados.keys()))):
                    AuxTexto.append("  Estado: "+str(key)+" -->  "+str(self.DiccionarioObjetos[i].estados.get(key).transiciones))
                
                AuxTexto.append("")

            tk.Label(ventana, text="Trasiciones de los AFN actuales: ").place(x = 20, y = 20)

            texto = tk.Listbox(ventana, height = 12 , width = 55 )
            texto.insert(tk.END,*AuxTexto)
            texto.place(x = 20, y = 40)

        if tipo_ventana == "Analizador":
            Elementos = list(self.DiccionarioObjetos.keys())
            self.AFD = self.DiccionarioObjetos[Elementos[0]].ir_a()

            print("AFD-------------------------")
            print(self.AFD.estados)
            print(self.AFD.finales)
            print(self.AFD.transiciones)
             
            messagebox.showinfo(message="La conversion AFN --> AFD fue Exitosa", title="Confirmacion", parent = ventana)

            tk.Label(ventana, text="Cadena: ").place(x = 20, y = 20)

            Cadena = tk.Entry(ventana,width = 40)
            Cadena.place(x = 80, y = 20 )

            tk.Button(ventana, text="Analizar", height = 1, width = 5, activebackground = "blue", activeforeground = "White",command = lambda: AlgoritmoLex(Cadena.get(),Resultados,self.AFD)).place( x = 415, y = 15)

            tk.Label(ventana, text="Tabla del AFD ").place(x = 80, y = 45)
            listaTablaReglas = tk.Listbox(ventana,height = 11 , width = 26)
            listaTablaReglas.place(x = 20, y = 60)

            ObtencionTablaAFD(self.AFD,listaTablaReglas)

            tk.Label(ventana, text="Resultado Analisis ").place(x = 300, y = 45)
            Resultados = tk.Listbox(ventana,height = 11 , width = 26)
            Resultados.place(x = 260, y = 60)

        tk.Button(ventana, text="Cerrar" , fg="red", command = ventana.destroy).place(x = 225, y = 250)

    def Mostrar(self):
        Elementos = list(self.DiccionarioObjetos.keys())

        for i in Elementos:
            Objeto = self.DiccionarioObjetos[i]
            Objeto.imprimir_transiciones()
