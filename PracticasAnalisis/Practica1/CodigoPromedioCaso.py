import numpy as np
import time
import matplotlib.pyplot as plt

def swap(Array,x,y):
    aux = Array[x]
    Array[x] = Array[y]
    Array[y] = aux

def InsertionSort():
    global A
    global TFinalInsert
    n = len(A)
    TInicial = time.time()
    for i in range(1,n):
        j = i - 1
        while j >= 0 and A[j] > A[j+1]:
            swap(A,j,j+1)
            j = j-1
    TFinal = time.time()
    TFinalInsert =  TFinal - TInicial

    

def Bubble():
    global B
    global TFinalBubble
    n = len(B)
    TInicial = time.time()
    while True:
        bandera = False
        for i in range(1,n):
            if B[i-1] > B[i]:
                swap(B,i-1,i)
                bandera = True
            
        n = n - 1
        if not bandera:
            break
    
    TFinal = time.time()
    TFinalBubble =  TFinal - TInicial


def Graficar():
    fig, ax = plt.subplots()
    ax.plot(Numeros, TiemposFinalesSort, label="Sort",color = 'blue')
    ax.plot(Numeros,TiemposFinalesBubble, label="Bubble",color= 'green')
    ax.legend()
    
    plt.title('Comparación Tiempos Peor Caso')
    plt.show()
   

    
#Inicio de Todo el Programa *****************************************************************************
TiemposFinalesSort = [] 
TiemposFinalesBubble = []  
Numeros = [] 
A = []
B = []
TFinalInsert = 0
TFinalBubble = 0

#Implementacion del arreglo 
for i in range(1,11):
    
    m = i*1000
    Numeros.append(m)
    cadenaAux ="/home/edgarmunguia/Documentos/TrabajosUniversidad/PracticasAnalisis/rand_case/rand_" + str(m)
    ArchivoDatos = open(cadenaAux,"r")
    for linea in ArchivoDatos:
        A.append(int(linea))
        B.append(int(linea))
    
    
    #Codigo Sort
    print("Para "+str(m)+": ")
    #print(A)
    InsertionSort()
    #print(A)
    TiemposFinalesSort.append(TFinalInsert)
    print("  Tiempo Sort :" + str(TFinalInsert))
    

    #Codigo Bubble
    #print(B)
    Bubble()
    #print(B)
    TiemposFinalesBubble.append(TFinalBubble)
    print("  Tiempo Bubble :" + str(TFinalBubble)+"\n")


Graficar()
