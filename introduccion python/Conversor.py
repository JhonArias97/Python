valor_dolar_1 = int(3750)
valor_dolar_2 = int(51)
valor_dolar_3 = int(169.76)
c = 0

def calculo (c):
    pesos = float(input("Cuantos pesos tienes?: "))
    dolares = pesos / c
    dolares =str(round(dolares, 2))
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 💵

1 = Pesos colombianos
2 = Pesos argentinos
3 = Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    c = valor_dolar_1
    calculo (c)
elif opcion == 2:
    c = valor_dolar_2
    calculo (c)
elif opcion == 3:
    c = valor_dolar_3
    calculo (c)



