import tkinter as tk
from Ventana import Crear_Ventanas

DiccionarioObjetos = {}
ventana_Menu = tk.Tk()
Menu = Crear_Ventanas(master=ventana_Menu)
Menu.create_widgets("Menu")
Menu.mainloop()