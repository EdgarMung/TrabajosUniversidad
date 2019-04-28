
def ObtencionNumerosBinarios(n):
	

def ObtencionTamañoBinario(MayorNumero,cont):
	while MayorNumero != 0:
		MayorNumero = int(MayorNumero / 2)
		cont = cont + 1	
		print(MayorNumero,cont)



def ObtencionNumeros(Ingresa,Salida):
	CadenaAuxiliar = ""

	n = len(Ingresa)
	
	for x in range(0,n):
		if Entrada[x] != ' ':
			CadenaAuxiliar+= Entrada[x]
		else:
			Salida.append(int(CadenaAuxiliar))
			CadenaAuxiliar = ""

	Salida.append(int(CadenaAuxiliar))


contador = 0
Numeros = []
Entrada = input("Ingresa la secuencia: ")
print(Entrada);
ObtencionNumeros(Entrada,Numeros)
ObtencionTamañoBinario(max(Numeros),contador)
ObtencionNumerosBinarios(contador)


