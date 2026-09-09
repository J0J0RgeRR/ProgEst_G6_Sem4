def clasGrade(n):
    if n <= 69:
        return "Aprendizaje inicial"
    elif n <= 79:
        return "Aprendizaje fundamental"
    elif n <= 89:
        return "Aprendizaje satisfactorio"
    else:
        return "Aprendizaje avanzado"


def countGrade(notas):
    for n in notas:
        print(n, "-", clasGrade(n))