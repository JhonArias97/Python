import random
zoom = ("f!Eaf#7c")
ecopetrol = ("0E3Bb$94")
misiontic = ("J0#&a9f#56e")
github = ("FG5&96d/#b")

def generar_contrasena(n):
    mayusculas = ["A", "B", "C", "D", "E", "F", "G"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g"]
    simbolos = ["!", "#", "$", "&", "/", "?"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    
    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for _ in range (n):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    n_caracteres = int(input("¿De cuantos caracteres deseas tu contraseña?"))
    contrasena = generar_contrasena(n_caracteres)
    print(f"tu nueva contaseña es {contrasena}")


if __name__ == "__main__":
    run()