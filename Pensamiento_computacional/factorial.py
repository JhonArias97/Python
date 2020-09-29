def run():
    def factorial(n) :
        """
        Calcula el factorial de n.

        n int > 0
        return n!
        """
        if n == 1:
            return 1
        return n * factorial (n - 1)

    a = int(input("Escribe un numero: "))
    
    print(factorial(a))

if __name__ == "__main__":
    run()