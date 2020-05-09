matrices = [[30,35],[35,15],[15,5],[5,10],[10,20],[20,25]]

def InsertionSort():
    global Lista_1
    n = len(Lista_1)
    for i in range(1,n):
        j = i - 1
        while j >= 0 and Lista_1[j][1] < Lista_1[j+1][1]:
            swap(Lista_1,j,j+1)
            j = j-1

def swap(Array,x,y):
    aux = Array[x][1]
    Array[x][1] = Array[y][1]
    Array[y][1] = aux

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

#ingresoDatos()

Lista_1 = matrices[:]

for i in Lista_1:
    print(i)

InsertionSort()

print("------------")
for i in Lista_1:
    print(i)