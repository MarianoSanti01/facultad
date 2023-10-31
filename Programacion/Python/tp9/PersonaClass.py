class Persona:
    
    def __init__(self,name='',age=0,dni=''):
        self.name=name
        self.age=age
        self.dni=dni


    def getname(self):
        return self.name
    
    def setname(self,name):
        if isinstance(name,str):
            self.name=name
        else:
            print("Error: El nombre debe ser una cadena de texto")


    def getage(self):
        return self.age
    
    def setage(self,age):
        if isinstance(age,int) and age>=0:
            self.age=age
        else:
            print("Error: La dead debe ser un numero entero")


    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 8:
            self.dni = dni
        else:
            print("Error: El DNI debe ser una cadena de 9 caracteres.")


    def mostrar(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"DNI: {self.dni}")


    def esMayorDeEdad(self):
        return self.age>=18