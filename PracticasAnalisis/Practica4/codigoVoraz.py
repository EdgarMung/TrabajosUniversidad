matrices = [[30,35],[35,15],[15,5],[5,10],[10,20],[20,25]]

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
    #print(Entrada.split(","))
    aux = Entrada.split(",")

    for i in aux:
        intermediario = i.split("x")
        #intermediario_B.append(int)
        matrices.append([int(intermediario[0]),int(intermediario[1])])

Lista_1,Lista_2 = InsertionSort(matrices)
