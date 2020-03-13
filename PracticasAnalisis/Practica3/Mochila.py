import numpy as np

def ObtencionSolucion(tabla,i,j,solucion):
    x = len(i[0])
    y = len(j) - 1

    while x >= 1:
        if tabla[x-1][y] == tabla[x][y]:
            x = x-1
        else:
            solucion[x-1] = 1
            x = x-1
            y = y - i[0][x]

def ObtencionValor(tabla,i,j,x,y):
    valor1 = tabla[x-1][y]
    
    aux = j[y]-i[0][x-1]
    if 0 > aux:
        valor2 = 0
    else:
        valor2 = tabla[x-1][aux]+i[1][x-1]

    if valor1 >= valor2:
        return valor1
    else:
        return valor2

def IngresoDatos(pesos,valores): # Operacion que realiza la carga de datos desde el archivo
    global W

    archivo = open('./datos',"r")
    
    aux = str(archivo.readline())
    ListaAux = aux.split(" | ")
    
    auxPesos = ListaAux[0].split(",")
    for elemento in auxPesos:
        pesos.append(int(elemento))

    auxValores = ListaAux[1].split(",")
    for elemento in auxValores:
        valores.append(int(elemento))

    W = int(ListaAux[2])

def sumaFinal(valores,solucion): # Operacion suma los valores de la cantidad de cada objeto que se hizo
    suma = 0
    
    for i in range(0,len(valores)):
        suma += solucion[i] * valores[i]

    return suma

def MochilaVoraz(pesos,valores,pesoLimite,n): # Algoritmo Voraz 
    valor_peso = []
    x = np.zeros(n,dtype=float)
    peso = 0



    for i in range(0,n):
        valor_peso.append(valores[i]/pesos[i])

    while peso < pesoLimite:
        mayor = max(valor_peso)
        j = valor_peso.index(mayor)
        valor_peso[j] = 0
        if (peso +  pesos[j]) <= pesoLimite:
            x[j] = 1
            peso = peso + pesos[j]
        else:
            x[j] = (pesoLimite-peso)/pesos[j]
            peso = pesoLimite

    return x
    
def MochilaProgramacionDinamica(pesos,valores,W):#  Algoritmo con Programación Dinamica
    solucion = np.zeros(len(pesos),dtype=int)
    tabla = np.zeros((len(pesos)+1,W+1),dtype = int)
    i = np.array((pesos,valores)) # 0 -> Pesos, 1 -> valores
    j = np.array(range(0,W+1))
    
    for x in range(1,len(i[0])+1):
        for y in range(1,len(j)):
            tabla[x][y] = ObtencionValor(tabla,i,j,x,y)
    
    print(tabla) 
    ObtencionSolucion(tabla,i,j,solucion)

    return solucion
               
# Inicio programa ----------------------------------------------------------------------------------------------------------
pesos = []
valores = []
W = 0

IngresoDatos(pesos,valores)


solucionVoraz = MochilaVoraz(pesos,valores,W,len(pesos))
sumaVoraz = sumaFinal(valores,list(solucionVoraz))

print("Peso Limite = " + str(W))

print("Resultados de programació Voraz: ")
print(" Peso de cada unidad = " + str (pesos))
print(" Valor de cada unidad = " + str(valores))
print(" sol = " + str(list(solucionVoraz)))
print(" suma = " + str(sumaVoraz),end="\n\n\n\n")

solucionDinamica = MochilaProgramacionDinamica(pesos,valores,W)
sumaDinamica = sumaFinal(valores,list(solucionDinamica))

print("Resultados de programació Voraz: ")
print(" Peso de cada unidad = " + str (pesos))
print(" Valor de cada unidad = " + str(valores))
print(" sol = " + str(list(solucionDinamica)))
print(" suma = " + str(sumaDinamica))

