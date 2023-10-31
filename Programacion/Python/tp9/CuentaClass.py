class Account:

    def __init__(self,headline="",amount=0.0):
        self.headline=headline
        self.amount=amount

    def getheadline(self):
        return self.headline
    def setheadline(self,headline):
        if isinstance(headline,str) and headline=="":
            self.headline=headline
        else:
            print("ERROR, EL TITULAR ES OBLIGATORIO")

    def getamount(self):
        return self.amount
    def setamount(self,amount):
        if isinstance(amount,float) and amount >= 0:
            self.amount=amount
        else:
            print("ERROR, Debe colocar un valor numerico mayor a 0")

    def mostrarac(self):
        print(f"Titular: {self.headline}")
        print(f"Dinero en cuenta: {self.amount}")

    def ingresar(self,amount):
        if amount > 0:
            self.amount += amount

    def retirar(self,amount):
        if amount > 0:
            self.amount -= amount