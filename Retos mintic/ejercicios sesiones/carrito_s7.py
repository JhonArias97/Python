from math import pi

def area_rectangulo(base, altura):
    area_r = base * altura
    return area_r

def area_circulo(radio):
    area_c = pi * radio * radio 
    return area_c

def run():
    a1 = float(input())
    b1 = float(input())
    a2 = float(input())
    b2 = float(input())
    r1 = float(input())
    r2 = float(input())
    area_r1 = area_rectangulo(a1,b1)
    area_r2 = area_rectangulo(a2,b2)
    area_c1 = area_circulo(r1)
    area_c2 = area_circulo(r2)
    area_t = area_r1 + area_r2 + area_c1 + area_c2
    print (f"suma total = {area_t}")

if __name__ == "__main__":
    run()
