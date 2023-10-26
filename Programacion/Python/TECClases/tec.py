from Motocicleta import Motorcycle
##Declaro las motos, y todos sus valores
m1=Motorcycle("Rojo",'La malvada',10,2,'Motomel','La mas nueva','24/10/2023',200,150)
m2=Motorcycle("Amarillo",'Patito',20,3,'Motomel','La mas vieja','24/10/1980',150,200)
m3=Motorcycle("Verde",'Pasto',10,2,'Harley Davison','Moto yankee','15/8/2020',180,180)

#Imprimo la definicion de cada una
print(f"La moto numero 1 es de color {m1.color}, patente {m1.registration}, cuenta con {m1.fuel_liters} de nafta, tiene {m1.number_of_wheels} ruedas, es de marca {m1.make} y modelo {m1.model}, fabricada {m1.manufacturing_date}, alcanza {m1.top_speed} km/h, y pesa {m1.weight}, su estado es {m1.state}")

print(f"La moto numero 2 es de color {m2.color}, patente {m2.registration}, cuenta con {m2.fuel_liters} de nafta, tiene {m2.number_of_wheels} ruedas, es de marca {m2.make} y modelo {m2.model}, fabricada {m2.manufacturing_date}, alcanza {m2.top_speed} km/h, y pesa {m2.weight}, su estado es {m2.state}")

print(f"La moto numero 3 es de color {m3.color}, patente {m3.registration}, cuenta con {m3.fuel_liters} de nafta, tiene {m3.number_of_wheels} ruedas, es de marca {m3.make} y modelo {m3.model}, fabricada {m3.manufacturing_date}, alcanza {m3.top_speed} km/h, y pesa {m3.weight}, su estado es {m3.state}")

#Hago la prueba de motor con la moto numero 1
m1.start_up()
m1.stop()

#Le pongo precio a la moto numero
m3.price=25000


#Imprimo el precio desde la clase
m3.print_price()
m1.print_price()
m2.print_price()
