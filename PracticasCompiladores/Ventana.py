import tkinter as tk
from PIL import Image , ImageTk

class Crear_Ventanas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.DiccionarioObjetos = {}
        self.master.geometry("400x550")
        self.master.title("Compiladores")
        self.pack()

    def create_widgets(self,tipo_Ventana):

        if tipo_Ventana == "Menu":
            tk.Button(self, text="AFN Basico", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("AFN Simple",self.master)).pack()
            tk.Button(self, text="Union", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold").pack()
            tk.Button(self, text="Concatenacion", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold").pack()
            tk.Button(self, text="Cerradura Positiva", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold").pack()
            tk.Button(self, text="Cerradura Kleene", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold").pack()
            tk.Button(self, text="Opcional", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold").pack()
            self.quit = tk.Button(self, text="Cerrar" , fg="red", command=self.master.destroy)
            self.quit.pack(side="bottom")

    def create_second_window(self,tipo_ventana,root):
        ventana = tk.Toplevel(root)
        if tipo_ventana == "AFN Simple":
            aux = Image.open("./Imagenes/Prueba.jpg")
            img = ImageTk.PhotoImage(aux.resize((150, 100), Image.ANTIALIAS))
            
            ventana.geometry("500x300")
            ventana.title("Operación "+tipo_ventana)
            tk.Label(ventana, text="Por favor, Ingrese el caracter del AFN Simple: ").place(x = 50, y = 50)
            tk.Entry(ventana,width = 10).place(x = 335, y = 50 )
            Lista = tk.Listbox(ventana)
            Lista.insert(tk.END,"Esta webada ya quedo")
            Lista.place(x = 50, y = 70)
            tk.Label(ventana,image = img).place(x = 250 , y =70)

            

            
             

    def IngresarAFNDiccionario(self,Diccionario):
        pass
