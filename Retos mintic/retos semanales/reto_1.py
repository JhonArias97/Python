def run():
    producto = input("Introduce el nombre del prodocuto: ")
    costo = int(input("Introduce el costo unitario: "))
    precio = int(input("Introduce el precio de venta: "))
    unidades = int(input("Introduce las unidades disponibles: "))
    ganacias = (precio - costo) * unidades

    print(f'Producto: {producto}')
    print(f'CU: ${costo}')
    print(f'PVP: ${precio}')
    print(f'Unidades Disponibles: {unidades}')
    print(f'Ganancia: ${ganacias}')



if __name__ == "__main__":
    run()