import time

def PrimerFiltro():
	global Tabla_Ecuaciones_D
	global Tabla_Ecuaciones_T
	global Tabla_Ecuaciones_JK
	
	bandera_uno = 0
	bandera_cero = 0

	#Tabla D
	for i in range(0,contador):
		bandera_uno = 0
		bandera_cero = 0
		for j in range(0,TotalDeNumeros):
			if Tabla_D[j][i] == '1':
				bandera_uno+=1
				#print("Si_uno"+str(i)+str(j))
			else:
				#print("Si_Cero"+str(i)+str(j))
				bandera_cero+=1

		if bandera_cero == TotalDeNumeros:
			Tabla_Ecuaciones_D[i] = '0'
		elif bandera_uno == TotalDeNumeros:
			Tabla_Ecuaciones_D[i] = '1'

	#Tabla T
	for i in range(0,contador):
		bandera_uno = 0
		bandera_cero = 0
		for j in range(0,TotalDeNumeros):
			if Tabla_T[j][i] == '1':
				bandera_uno+=1
				#print("Si_uno"+str(i)+str(j))
			else:
				#print("Si_Cero"+str(i)+str(j))
				bandera_cero+=1

		if bandera_cero == TotalDeNumeros:
			Tabla_Ecuaciones_T[i] = '0'
		elif bandera_uno == TotalDeNumeros:
			Tabla_Ecuaciones_T[i] = '1'

	#Tabla JK
	for j in range(0,len(Tabla_Ecuaciones_T)):
		Tabla_Ecuaciones_JK[j] = Tabla_Ecuaciones_T[j]
		
def ConversorNumerosBinariosAVariables(NumeroBinario,n):
	CadenaConversion = ""

	for i in range(0,n):
		if NumeroBinario[i] == '1':
			CadenaConversion+=chr(65+i)
		else:
			CadenaConversion+="("+chr(65+i)+"')"
	return CadenaConversion

def MostrarEcuaciones(Extra):
	print("\n\nEcuaciones Obtenidas de Las tabla"+Extra+"\n")
	print("  Flip_Flop Tipo D: ")
	for i in range(0,len(Tabla_D[0])):
		print("   D"+chr(65 + i)+" = " + Tabla_Ecuaciones_D[i])

	print("\n  Flip_Flop Tipo T: ")
	for i in range(0,len(Tabla_D[0])):
		print("   T"+chr(65 + i)+" = " + Tabla_Ecuaciones_T[i])

	print("\n  Flip_Flop Tipo JK: ")
	for i in range(0,len(Tabla_D[0])):
		print("   JK"+chr(65 + i)+" = " + Tabla_Ecuaciones_JK[i])

def MostrarTablas():

	CadenaAuxiliar = "  "
	for i in range(0,len(NumerosBinarios[0]*2)+3):
		CadenaAuxiliar+="_"
	
	CadenaAuxiliar+="_|  D"

	for i in range(0,len(NumerosBinarios[0])-2):
		CadenaAuxiliar+=" "


	CadenaAuxiliar+=" |  T"

 
	for i in range(0,len(NumerosBinarios[0])-2):
		CadenaAuxiliar+=" " 

	CadenaAuxiliar+=" |  JK"

	print("\nTablas Que Muestran El rasultado De Cada Flip_Flop")
	print(CadenaAuxiliar)

	CadenaAuxiliar = ""
	CadenaAuxiliarJK = ""
	for y in range(0,len(NumerosBinarios[0])):
		CadenaAuxiliar+=chr(65+y)
		CadenaAuxiliarJK+=chr(65+y)
		CadenaAuxiliarJK+=chr(65+y)
		CadenaAuxiliarJK+=" "



	print("  "+CadenaAuxiliar+" | "+CadenaAuxiliar+" | "+CadenaAuxiliar+" | "+CadenaAuxiliar+" | "+CadenaAuxiliarJK.rstrip("  "))
	
	for j in range(0,TotalDeNumeros):
		print("  "+NumerosBinarios[j]+" | "+MatrizFutura[j]+" | "+Tabla_D[j]+" | "+Tabla_T[j]+" | "+Tabla_JK[j])

def ObtencionEcuaciones_D_T_JK():
	global Tabla_Ecuaciones_D
	global Tabla_Ecuaciones_T
	global Tabla_Ecuaciones_JK

	#Obtencion Tabla de Ecuaciones De la Tabla D 
	for i in range(0,contador):
		CadenaAuxiliar = ""
		for j in range(0,TotalDeNumeros):
			if  Tabla_D[j][i] == '1':
				CadenaAuxiliar+=ConversorNumerosBinariosAVariables(NumerosBinarios[j],len(NumerosBinarios[j]))
				CadenaAuxiliar+="+"
		Tabla_Ecuaciones_D.append(CadenaAuxiliar.rstrip("+"))

	#Obtencion Tabla de Ecuaciones De la Tabla T 
	for i in range(0,contador):
		CadenaAuxiliar = ""
		for j in range(0,TotalDeNumeros):
			if  Tabla_T[j][i] == '1':
				CadenaAuxiliar+=ConversorNumerosBinariosAVariables(NumerosBinarios[j],len(NumerosBinarios[j]))
				CadenaAuxiliar+="+"
		
		Tabla_Ecuaciones_T.append(CadenaAuxiliar.rstrip("+"))

	#Obtencion Tabla de Ecuaciones De la Tabla JK
	for j in range(0,len(Tabla_Ecuaciones_T)):
		Tabla_Ecuaciones_JK.append(Tabla_Ecuaciones_T[j])

def ObtencionTablas_D_T_JK():
	global Tabla_D
	global Tabla_T
	global Tabla_JK

	#Obtencion de la tabla tipo D
	for j in range(0,TotalDeNumeros):
		Tabla_D.append(MatrizFutura[j])

	#Obtencion tabla toggle
	for j in range(0,TotalDeNumeros):
		CadenaAuxiliar = ""
		for i in range(0,contador):
			if NumerosBinarios[j][i] == MatrizFutura[j][i]:
				CadenaAuxiliar+='0'
			else:
				CadenaAuxiliar+='1'

		Tabla_T.append(CadenaAuxiliar)

	#Obtencion Tabla JK
	for j in range(0,TotalDeNumeros):
		CadenaAuxiliar = ""
		for i in range(0,contador):
			if NumerosBinarios[j][i] == MatrizFutura[j][i]:
				CadenaAuxiliar+='00 '
			else:
				CadenaAuxiliar+='11 '

		Tabla_JK.append(CadenaAuxiliar.rstrip(" "))

def ObtencionMarizFuturo(MatrizPresente,n):
	global MatrizFutura

	for i in range(0,n-1):
		MatrizFutura.append(MatrizPresente[i+1])

	MatrizFutura.append(MatrizPresente[0])

def ObtencionNumerosBinarios(logitud,TotalDeNumeros):
	Numero = 0
	CadenaAuxiliar = ""
	for i in range(0,TotalDeNumeros):
		Numero = Numeros[i]
		for j in range(0,logitud):
			if Numero == 0:	
				CadenaAuxiliar+= '0'
			else:
				CadenaAuxiliar+= str(Numero % 2)
				Numero = int(Numero / 2)
			
		NumerosBinarios.append(CadenaAuxiliar[::-1])
		CadenaAuxiliar = ""
 	
def ObtencionTamañoBinario(MayorNumero):
	global contador
	while MayorNumero != 0:
		MayorNumero = int(MayorNumero / 2)
		contador = contador + 1

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
NumerosBinarios = []
MatrizFutura = []
Tabla_D = []
Tabla_T = []
Tabla_JK = []
Tabla_Ecuaciones_D = []
Tabla_Ecuaciones_T = []
Tabla_Ecuaciones_JK = []
CadenaAuxiliar = ""


Entrada = input("Ingresa la secuencia: ")
print("\n La Secuencia que ingresaste es: "+Entrada);
ObtencionNumeros(Entrada,Numeros)
TotalDeNumeros = len(Numeros)
ObtencionTamañoBinario(max(Numeros))
ObtencionNumerosBinarios(contador,TotalDeNumeros)
ObtencionMarizFuturo(NumerosBinarios,TotalDeNumeros)
ObtencionTablas_D_T_JK()
MostrarTablas()
ObtencionEcuaciones_D_T_JK()
MostrarEcuaciones("")
PrimerFiltro()
MostrarEcuaciones(" Despues Del Primer Filtro")

