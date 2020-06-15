def G():
    if(ListaReglas()):
        return True
    return False

def ListaReglas():
    if(Regla()):
        Lexico
        if (ListaReglas()):
            return True
    return False

def Regla():
    if(LadoIzq()):
        return True
    return False

def LadoIzq():
    return True

print(G())