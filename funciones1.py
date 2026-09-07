#Leer la edad de una persona y dicernir si es mayor de edad o menor de edad
age=0
def check_age():
    print("Ingrese su edad: ")
    global age
    age=int(input())

def evaluate_age(age):
    return  age >= 18

def show():
    global age
    print("Usted es mayor de edad" if evaluate_age(age) else "Usted es menor de edad")

check_age()
show()