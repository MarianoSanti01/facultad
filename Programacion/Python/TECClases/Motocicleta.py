class Motorcycle:
    # defino fuera del init el estado de la moto y el motor. para qué su valor no cambie
    state="Nueva"
    motor=False

    #Coloco los self para todos los valores
    def __init__(self,color,registration, fuel_liters, number_of_wheels, make, model, manufacturing_date, top_speed, weight):
        self.color=color
        self.registration=registration
        self.fuel_liters=fuel_liters
        self.number_of_wheels=number_of_wheels
        self.make=make
        self.model=model
        self.manufacturing_date=manufacturing_date
        self.top_speed=top_speed
        self.weight=weight

#Metodo para prender la moto
    def start_up(self):
        if (self.motor==False):
            self.motor=True
            print("Usted arrancó su moto")
        else:
            print("El motor ya está arrancado")

#Metodo para apagar la moto
    def stop(self):
        if (self.motor==True):
            self.motor=False
            print("Usted paró la moto")
        else:
            print("El motor ya está detenido")

#Metodo para imprimir el precio
    def print_price(self):
        print(f"El precio de la motocicleta {self.make} modelo {self.model} es de {self.price}")

