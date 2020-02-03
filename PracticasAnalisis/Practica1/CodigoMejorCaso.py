import numpy as np
import time
import matplotlib.pyplot as plt

def swap(Array,x,y):
    aux = Array[x]
    Array[x] = Array[y]
    Array[y] = aux

def InsertionSort():
    global A
    for i in range(1,len(A)):
        j = i - 1
        while j >= 0 and A[j] > A[j+1]:
            swap(A,j,j+1)
            j = j-1

def Bubble():
    global B
    n = len(B)
    while True:
        bandera = False
        for i in range(1,n):
            if B[i-1] > B[i]:
                swap(B,i-1,i)
                bandera = True
            
        n = n - 1
        if not bandera:
            break
 
def Graficar():
    fig, ax = plt.subplots()
    ax.plot(Numeros, TiemposFinalesSort, label="Sort",color = 'blue')
    ax.plot(Numeros,TiemposFinalesBubble, label="Bubble",color= 'green')
    ax.legend()
    
    plt.title('Comparación Tiempos Peor Caso')
    plt.show()
   

    
#Inicio de Todo el Programa
TiemposFinalesSort = [] 
TiemposFinalesBubble = []  
Numeros = []          

for i in range(1,11):
    
    m = i*1000
    Numeros.append(m)
    #Implementacion del arreglo
    A = np.arange(m)
    B = np.arange(m)

    #Codigo Sort
    print("Para "+str(m)+": ")
    TInicialInsert = time.time()
    InsertionSort()
    TFinalInsert = time.time() - TInicialInsert
    TiemposFinalesSort.append(TFinalInsert)
    print("  Tiempo Sort :" + str(TFinalInsert))
    

    #Codigo Bubble
    TInicialBubble = time.time()
    Bubble()
    TFinalBubble = time.time() - TInicialBubble
    TiemposFinalesBubble.append(TFinalBubble)
    print("  Tiempo Bubble :" + str(TFinalBubble)+"\n")


Graficar()
