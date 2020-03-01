import tkinter as tk
from tkinter import ttk
from sympy import integrate, exp,cos,log
from sympy.abc import x
import random
import math
import numpy as np
from matplotlib import pyplot as plt

def f1(x,funcion):
    if funcion == 0:
        return ( 1 - x**2 )**( 3/2 )
    elif funcion == 1:
        return math.exp( x + x**2 )
    elif funcion == 2:
        return (1 + x**2 )**2
    elif funcion == 3:
        return 1/(math.cos(x) + 2)
    elif funcion == 4:
        return math.log(x)

def aprox_integral(n, b, a,Mostrar,funcion):
    Parte_x = []
    Parte_y = []
    sum  = 0
    for i in range(0, n):
        ui = random.uniform(0, 1)
        operacion = ui*(b-a) + a
        resultadoFuncion = f1(operacion,funcion)
        sum  = sum + resultadoFuncion
        Parte_x.append(operacion)
        Parte_y.append(resultadoFuncion)
    
    resultado = (b-a)/n * sum

    Mostrar.config(state="normal")
    Mostrar.delete(1.0, tk.END)
    Mostrar.insert(tk.END,resultado)
    Mostrar.config(state="disabled")    

    Parte_x.append(resultado)
    Parte_y.append(resultado)
    
    plt.cla()
    plt.plot(Parte_x,Parte_y,"b*")
    plt.show()


def CalculoIntegralExacta(funcion,LimiteInferior,LimiteSuperior,Mostrar):
    
    resultado = float(integrate(Funciones[funcion], (x,float(LimiteInferior),float(LimiteSuperior))))
 
    Mostrar.config(state="normal")
    Mostrar.delete(1.0, tk.END)
    Mostrar.insert(tk.END,resultado)
    Mostrar.config(state="disabled")


Elementos = ["( 1 - (x²))^(3/2)","e^(x + x²)","(1 + x²)²","1/(cos(x)+2)","log(x)"]
Funciones = [(1-x**2)**(3/2) , exp(x+x**2) , (1 + x**2)**2 , 1/(cos(x)+2) , log(x)]
Parte_x = []
Parte_y = []

ventana = tk.Tk()
ventana.title("Interfaz Integrales")
ventana.config(bg = "floral white")

fig = plt.figure()
Grafico = plt.axes()
plt.plot(Parte_x, Parte_y)
plt.xlabel('x label')
plt.ylabel('y label')
plt.xlim(-3,3)
plt.ylim(-3,3)

plt.title("Simulación")

ParteTitulo = tk.Frame(ventana,bd = 10,bg = "floral white")
ParteTitulo.pack()
tk.Label(ParteTitulo,text="Aproximación Integrales por el Metodo Monte Carlo", borderwidth=2, relief="solid", font=("HVD Bodedo",10),bg = "floral white").pack()

ParteEntradas = tk.Frame(ventana, bd = 10,bg = "floral white") 
ParteEntradas.pack()

tk.Label(ParteEntradas,text="Seleccione integral: ",bg = "floral white").grid(row = 0,column = 0)
Opciones = ttk.Combobox(ParteEntradas,state = "readonly",values = Elementos , width = 20)
Opciones.grid(row = 0,column = 1,columnspan= 4 )

tk.Label(ParteEntradas,text="Rangos   -> ",bg = "floral white").grid(row = 1,column = 0,sticky = 'W')
LimiteInferior = tk.Entry(ParteEntradas,width = 10)

tk.Label(ParteEntradas,text="a: ",bg = "floral white",width = 4).grid(row = 1,column = 1)
LimiteInferior.grid(row = 1,column = 2)
tk.Label(ParteEntradas,text="b: ",bg = "floral white",width = 4).grid(row = 1,column = 3)
LimiteSuperior = tk.Entry(ParteEntradas,width = 10)
LimiteSuperior.grid(row = 1,column = 4)

tk.Button(ParteEntradas, text=" Calcular Integral Exacta", height = 1, activebackground = "blue", activeforeground = "White",command = lambda: CalculoIntegralExacta(Opciones.current(),LimiteInferior.get(),LimiteSuperior.get(),TextoIntegralExacta)).grid(row = 0,column = 5)
TextoIntegralExacta = tk.Text(ParteEntradas,width = 20,height = 1)
TextoIntegralExacta.insert(tk.END,"Solucion ")
TextoIntegralExacta.config(state = "disabled")
TextoIntegralExacta.grid(row = 1,column = 5)

ParteSimulacion = tk.Frame(ventana,bd = 10,bg = "floral white")
ParteSimulacion.pack()
tk.Label(ParteSimulacion,text="Ingrese numero de aleatorios(N) : ",bg = "floral white").grid(row = 0,column = 0)
N = tk.Entry(ParteSimulacion,width = 15)
N.grid(row = 0,column = 1)
tk.Button(ParteSimulacion, text=" Calcular Integral Aproximada", height = 1, activebackground = "blue", activeforeground = "White",command = lambda: aprox_integral(int(N.get()),float(LimiteSuperior.get()),float(LimiteInferior.get()),TextoIntegralAproximado,Opciones.current())).grid(row = 0,column = 2)

tk.Label(ParteSimulacion,text="Resultado Aproximado : ",bg = "floral white").grid(row = 1,column = 0)
TextoIntegralAproximado = tk.Text(ParteSimulacion,width = 20,height = 1)
TextoIntegralAproximado.insert(tk.END,"Solucion ")
TextoIntegralAproximado.config(state="disabled")
TextoIntegralAproximado.grid(row=1,column=1)

ventana.mainloop()