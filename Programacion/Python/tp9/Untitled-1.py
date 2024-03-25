from tkinter import *
def tranqui():
    print("Hola mariano")
root = Tk()
message = Label(text="Hola Mariano").pack()
button = Button(command=tranqui).pack()

root.mainloop()