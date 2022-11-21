import random

randomNumber = random.randint(1, 50)
tries = 1
print("Bienvenido a Guess the Number")
print("Aleatoriamente se ha elegido un numero entre el 1 y el 50 " +
      "tu mision sera adivinar dicho numero en el menor numero de intentos posible")
userInput = int(input("Ingresa un numero: "))
while userInput != randomNumber:
    while userInput < 1 or userInput > 50:
        print("Por favor, solo ingresa numeros dentro del rango (1-50) este intento no contara")
        userInput = int(input("Ingresa un numero: "))
        if userInput == randomNumber:
            print(f"Felicidades, has adivinado en {tries} intentos, el numero secreto era {randomNumber}")
            exit()
    print("Lo siento, intento fallido de adivinar :(, intenta de nuevo")
    tries += 1
    userInput = int(input("Ingresa un numero: "))
if userInput == randomNumber:
    print(f"Felicidades, has adivinado en {tries} intentos, el numero secreto era {randomNumber}")
    exit()
