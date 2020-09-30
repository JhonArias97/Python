
def run():
    pass

val_a = int(input(""))
val_b = int(input(""))
val_c = int(input(""))
val_d = int(input(""))

if (val_b > val_c and val_d > val_a) and (val_c + val_d > val_a + val_b) and (val_c >= 0 and val_d >= 0) and (val_a % 2 == 0):
    print("Valores aceptados")
else:
    print("Valores no aceptados")

if __name__ == "__main__":
    run()