class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def determinar_tipo(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilátero"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Isósceles"
        else:
            return "Escaleno"

    def imprimir_lado_mayor(self):
        mayor= max(self.side1, self.side2, self.side3)
        print(f"El lado con mayor longitud es {mayor}")