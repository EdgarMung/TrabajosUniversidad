import tkinter as tk

class Crear_VentanaCalculadora(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x300")
        self.master.title("Calculadora")

    def widges(self):
        tk.Label(self.master, text="Cadena: ").place(x = 20, y = 20)
        cadena = tk.Entry(self.master,width = 40)
        cadena.place(x = 80, y = 20 )
        tk.Label(self.master, text="Resultado Lexico").place(x = 77, y = 43)
        listaTablaReglas = tk.Listbox(self.master,height = 11 , width = 26)
        listaTablaReglas.place(x = 20, y = 60)
        tk.Button(self.master, text="Analizar", height = 1, width = 5, activebackground = "blue", activeforeground = "White").place( x = 90, y = 245)




