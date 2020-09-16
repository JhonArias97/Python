import random



def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    while numero_aleatorio != numero_elegido:
        if numero_aleatorio < numero_elegido:
            print("Busca un numero mas pequeño")
        else:
            print("Busca un numero mas grande")
        numero_elegido = int(input("Elige otro numero: "))
    print("¡ganaste!")



if __name__ == "__main__":
    run()