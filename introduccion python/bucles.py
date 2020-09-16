def run ():
    a = 0
    n = 1
    while n < 1000:
        print (f"2 elevado a {a} es igual a {n}" )
        a = a + 1
        n = 2 ** a

if __name__ == "__main__":
    run ()

