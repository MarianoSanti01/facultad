from bingofunctions import*
cardboard = []
numsung= []
for i in range(5):
    cardboardfile=[]
    for i in range(5):
        num=num_obt()
        while num in cardboard or num in cardboardfile:
            print("Este numero ya fue ingresado.")
            num=num_obt()
        cardboardfile.append(num)
    cardboard.append(cardboardfile)


for i in range(5):
    print(cardboard[i])