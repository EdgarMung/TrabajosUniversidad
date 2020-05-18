matrices = [[30,35],[35,15],[15,5],[5,10],[10,20],[20,25]]

def SegundoFiltro(Elementos_1,Elementos_2):
    global suma
    posicion = -1

    while len(Elementos_1) + posicion >= 0 :
        bandera = 0
        Aj = Elementos_1[posicion]

        for Elemento in Elementos_1:
            if Aj[0] == Elemento[1]:
                Ak = Elemento
                EliminarElemento(Lista_1,Aj,Ak)
                EliminarElemento(Lista_2,Ak,Aj)
                Elementos_1.append([Ak[0],Aj[1]])
                suma+= Ak[0]*Ak[1]*Aj[1]
                bandera = 1
                break
        if bandera == 0:
            posicion -= 1

def PrimerFiltro(Elementos_1,Elementos_2):
    global suma
    posicion = -1
    
    while len(Elementos_1) + posicion >= 0 :
        bandera = 0
        Aj = Elementos_1[posicion]

        for Elemento in Elementos_2:
            if Aj[0] == Elemento[1]:
                Ak = Elemento
                EliminarElemento(Lista_1,Aj,Ak)
                EliminarElemento(Lista_2,Ak,Aj)
                Elementos_1.append([Ak[0],Aj[1]])
                suma+= Ak[0]*Ak[1]*Aj[1]
                bandera = 1
                break
        if bandera == 0:
            posicion -= 1

def EliminarElemento(Lista,Elemento_1,Elemento_2):
    for i in Lista:
        if Elemento_1 == i:
            Lista.remove(Elemento_1)
            break
    
    for j in Lista:
        if Elemento_2 == j:
            Lista.remove(Elemento_2)
            break

def InsertionSort(Elementos):
    n = len(Elementos)
    for i in range(1,n):
        j = i - 1
        while j >= 0 and Elementos[j][1] < Elementos[j+1][1]:
            swap(Elementos,j,j+1)
            j = j-1

    Elementos_1 = Elementos[:]

    for i in range(1,n):
        j = i - 1
        while j >= 0 and Elementos[j][0] < Elementos[j+1][0]:
            swap(Elementos,j,j+1)
            j = j-1 
    
    Elementos_2 = Elementos[:]

    return Elementos_1,Elementos_2

def swap(Array,x,y):
    aux = Array[x]
    Array[x] = Array[y]
    Array[y] = aux

def ingresoDatos():
    print("\n  Ingresa las matrices separadas por comas ',' y meter las matrices con el formato AxB.")
    print("  Ejemplo: AxB,CxD,ExF,....")

    Entrada = input("\tIngresa las matrices: ")
    aux = Entrada.split(",")

    for i in aux:
        intermediario = i.split("x")
        #intermediario_B.append(int)
        matrices.append([int(intermediario[0]),int(intermediario[1])])

suma = 0
cadena = ""

Lista_1,Lista_2 = InsertionSort(matrices)
PrimerFiltro(Lista_1,Lista_2)
SegundoFiltro(Lista_1,Lista_2)

print("----------------")
print("suma: "+str(suma))

print("-----------------")
print("Lista 1")
for i in Lista_1:
    print(i)

print("------------------")
print("Lista 2")
for i in Lista_2:
    print(i)