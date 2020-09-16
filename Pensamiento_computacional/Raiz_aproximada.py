def run():
    objetivo = int(input("Escoge un numero: "))
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) <= epsilon:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}") 





if __name__ == "__main__":
    run()