
def contagio(poblacion_1, poblacion_2):
    """
    Esta funcion calcula la velocidad del contagio y retorna el dia que la poblacion 1 alcanza a la 2
    """
    dia = 1

    while poblacion_1 > poblacion_2:
        poblacion_1 = poblacion_1 + (poblacion_1 * 0.02)
        poblacion_2 = poblacion_2 + (poblacion_2 * 0.03)
        dia += 1

    return dia

    


if __name__ == "__main__":
    poblacion_1 = int(input())
    poblacion_2 = int(input())

    dia_sobrepasa = contagio(poblacion_1, poblacion_2)
    print(dia_sobrepasa)
