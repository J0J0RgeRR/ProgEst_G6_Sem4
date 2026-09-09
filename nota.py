import Fn as fun


def READNOTES():
    notas = []

    cantidad = int(input("¿Cuántas notas desea ingresar?: "))

    for i in range(cantidad):
        nota = int(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)

    return notas


def SHOWALLGRADES(notas):
    print("\nTodas las notas con su aprendizaje:")
    fun.countGrade(notas)


if __name__ == "__main__":
    notas = READNOTES()
    SHOWALLGRADES(notas)