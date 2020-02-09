class Persona():
    Nombre = "General"
    Apellido = "General"
    Cedula = "General"

    def __init__(self,Name,SecondName,Cedul):
        self.Nombre = Name
        self.Apellido = SecondName
        self.Cedula = Cedul

    def MostrarInformación(self):
        print(self.Nombre)
        print(self.Apellido)
        print(str(self.Cedula))

PrimeraPersona = Persona("Edgar","Munguia",123456)

PrimeraPersona.MostrarInformación()