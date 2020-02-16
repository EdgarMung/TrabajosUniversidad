#class Persona():
 #   Nombre = "General"
 #   Apellido = "General"
 #   Cedula = "General"

 #   def __init__(self,Name,SecondName,Cedul):
 #       self.Nombre = Name
 #       self.Apellido = SecondName
 #       self.Cedula = Cedul

 #   def MostrarInformación(self):
  #      print(self.Nombre)
  #      print(self.Apellido)
  #      print(str(self.Cedula))

#PrimeraPersona = Persona("Edgar","Munguia",123456)

#PrimeraPersona.MostrarInformación()

import tkinter as tk


def ingresar(texto):
    ventanaIngresar = tk.Toplevel(ventanaPrincipal)
    ventanaIngresar.title("Ingresar")
    ventanaIngresar.geometry("350x300")
    tk.Label(ventanaIngresar, text= texto,
             font=("Agency FB", 14)).place(x=50, y=50)

ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry('380x200')
tk.Button(ventanaPrincipal, text="Ingresar", command= lambda: ingresar("TODO OK"),
          font=("Agency FB", 14), width=10).place(x=130, y=30)
ventanaPrincipal.mainloop()