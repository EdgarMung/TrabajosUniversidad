import numpy as np

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
    Arreglo = np.zeros((n),dtype=int)

    for i in range(0,n):
        Arreglo[i] = -1

    return fibo(n-1,Arreglo)

numero = 40
print("Algoritmo 1: "+str(Algoritmo1(numero-1)))
print("Algoritmo 2: "+str(Algoritmo2(numero)))
print("Algoritmo 3: "+str(Algoritmo3(numero)))