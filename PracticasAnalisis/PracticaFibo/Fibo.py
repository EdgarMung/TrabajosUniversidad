import numpy as np
import time

def Algoritmo1(n):
    if n < 2:
        return n    
    else:
        return Algoritmo1(n-1)+Algoritmo1(n-2)
    

def Algoritmo2(n):
    aux = []
    if n < 2:
        return n    
    else:
        aux.append(0)
        aux.append(1)

        for i in range(2,n+1):
            aux.append(aux[i-1] + aux[i-2])

    return aux[n-1]

def fibo(n,arreglo):
    if n < 2:
        return n
    if arreglo[n-1] == -1:
        arreglo[n-1] = fibo(n-1,arreglo)
    if arreglo[n-2] == -1:
        arreglo[n-2] = fibo(n-2,arreglo)

    arreglo[n] = arreglo[n-1] + arreglo[n-2]

    return arreglo[n]

def Algoritmo3(n):
    global TInicial
    Arreglo = np.zeros((n),dtype=int)

    for i in range(0,n):
        Arreglo[i] = -1

    TInicial = time.time()
    return fibo(n-1,Arreglo)

numero = 50

TInicial = time.time()
Algoritmo1(numero-1)
TFinal = time.time()
tiempoAlgorimto1 =  TFinal - TInicial
print("Algoritmo 1: "+str(tiempoAlgorimto1))

TInicial = time.time()
Algoritmo2(numero)
TFinal = time.time()
tiempoAlgorimto2 =  TFinal - TInicial
print("Algoritmo 2: "+str(tiempoAlgorimto2))

Algoritmo2(numero)
TFinal = time.time()
tiempoAlgorimto3 =  TFinal - TInicial
print("Algoritmo 3: "+str(tiempoAlgorimto3))