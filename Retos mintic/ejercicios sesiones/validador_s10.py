
def invertida(tex_1,tex_2):
    """
    Esta funcion compara dos cadenas de texto y retorna si son o no iguales
    """
    tex_2 = tex_2[::-1]
    if tex_2 == tex_1:
        print("SI")
    else:
        print("NO")



if __name__ == "__main__":
    tex_1 = input("")
    tex_2 = input("")

    invertida(tex_1, tex_2)
