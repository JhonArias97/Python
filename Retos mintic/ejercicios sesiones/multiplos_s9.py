import math

def multiplos(n, m):
    """
    Esta funcion calcula los multiplos de m hasta n
    """
    n_multiplos = math.floor(n/m)
    contador = 0
    print("Los múltiplos son:")

    # while contador <= n_multiplos:
    #     multiplo = contador * m
    #     print(multiplo)

    #     contador += 1
    for i in range(n_multiplos+1):
        multiplo = i * m
        print(multiplo)




if __name__ == "__main__":
    n = int(input("Digite n:"))
    m = int(input("Digite m:"))

    multiplos_mn = multiplos(n, m)