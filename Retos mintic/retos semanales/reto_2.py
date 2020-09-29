import math

def generar_factura(n):
    """
    Pregunta primero el numero de articulos y luego pregunta que articulo es y su valor
    """
    precio_t = 0
    descuento = 0
    texto_f = ("")
    for i in range(n):
        nombre = input("")
        precio = int(input(""))
        precio_t += precio
        texto = (f"{nombre} ${precio}\n")
        texto_f = texto_f + texto
    
    if precio_t > 150000 and precio_t <= 300000:
        descuento = math.floor(precio_t * 0.1)
        precio_t = math.ceil(precio_t * 0.9)
    elif precio_t > 300000 and precio_t <= 700000:
        descuento = math.floor(precio_t * 0.15)
        precio_t = math.ceil(precio_t * 0.85)
    elif precio_t > 700000:
        descuento = math.floor(precio_t * 0.2)
        precio_t = math.ceil(precio_t * 0.8)
    else:
        precio_t = precio_t
        descuento = 0
    
    print("Centro Comercial Unaleño\nCompra más y Gasta Menos\nNIT: 899.999.063")
    print(f"{texto_f}Total: ${precio_t}")
    print(f"En esta compra tu descuento fue ${descuento}\nGracias por tu compra")




if __name__ == "__main__":
    n = int(input(""))
    factura = generar_factura(n)