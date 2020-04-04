import tkinter as tk
from Ventana import Crear_Ventanas

def abrirMenuGeneradorAFN():
    ventanaSecundaria = tk.Toplevel(ventana)
    Menu = Crear_Ventanas(master=ventanaSecundaria)
    Menu.create_widgets()

ventana = tk.Tk()
ventana.geometry("150x250")
ventana.title("Ventana Principal")

parteTitulo = tk.Frame(ventana,bd = 10,bg = 'floral white')
parteTitulo.pack(fill = 'both')
tk.Label(parteTitulo,text="Menu Principal", borderwidth=5, relief="groove", font=("Century Schoolbook L",10),bg = "floral white").pack(fill = 'both')
parteBotones = tk.Frame(ventana,bg = "blue")
parteBotones.pack(fill = 'both')
tk.Button(parteBotones,text="Generador AFNś",pady = 10, command=abrirMenuGeneradorAFN).pack()
tk.Button(parteBotones,text="Calculadora").pack()


ventana.mainloop()