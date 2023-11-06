def num_obt():
    while True:
        num = input("Ingrese un numero entre 1 y 75: ")
        if num.isdigit():
            num = int(num)
            if 1 <= num <= 75:
                return num
            else:
                print("El numero debe de estar entre 1 y 75.")
        else:
            print("Por favor, ingresa un numero valido.")