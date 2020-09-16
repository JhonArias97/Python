def es_pal (palabra):
    palabra = palabra.replace (" ", "").lower()
    palabra_inv = palabra[::-1]
    if palabra == palabra_inv:
        return True
    else:
        return False

def run():
    palabra = input("escribe una palabra")
    if es_pal(palabra):
        print ("Es palindromo")
    else:
        print ("No es palindromo")


if __name__ == "__main__":
    run()