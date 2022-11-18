def isOdd():
    print("Bienvenido a par o impar, ingresa un numero entre 1 y 1000 y descubre si es par o impar")
    number = int(input("Ingresa un numero: "))
    if number > 0 and number < 1001:
        if number % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")
    else:
        print("Ingresa un numero que cumpla con el rango indicado")


isOdd()
