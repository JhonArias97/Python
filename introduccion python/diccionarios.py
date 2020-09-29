


def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }

    print(mi_diccionario)
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])
    

    poblacion_paises = {
        "Argentina": 235345,
        "Brasil": 234546,
        "Colombia": 597533,
    }

    print(poblacion_paises["Colombia"])

    for n in poblacion_paises.keys():
        print(n)

    for n in poblacion_paises.values():
        print(n)

    for n, m in poblacion_paises.items():
        print(f"{n} tiene {m} habitantes")

if __name__ == "__main__":
    run()