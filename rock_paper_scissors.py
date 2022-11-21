import random


print("Bienvenido al clasico juego de piedra papel o tijeras.")
try:
    userInput = int(input("Selecciona ingresando un numero" +
                        ":\n1.Piedra\n2.Papel\n3.Tijeras\n"))
except:
    print("Ingresa solo numeros")
    exit()
while userInput < 1 or userInput > 3:
    try:
        print("Por favor, ingresa una opcion dentro del rango permitido  (1-3)")
        userInput = int(input("Intenta de nuevo: "))
    except:
        print("Ingresa solo numeros")


def jugar(userInput):
    print()
    cpuPick = random.randint(1, 3)
    match userInput:
        case 1:
            match cpuPick:
                case 1:
                    print("Has seleccionado piedra")
                    print("CPU ha seleccionado piedra")
                    print("Es un empate :|")
                case 2:
                    print("Has seleccionado piedra")
                    print("CPU ha seleccionado papel")
                    print("Has perdido :(")
                case 3:
                    print("Has seleccionado piedra")
                    print("CPU ha seleccionado tijeras")
                    print("Has ganado  :)!")
        case 2:
            match cpuPick:
                case 1:
                    print("Has seleccionado papel")
                    print("CPU ha seleccionado piedra")
                    print("Has ganado :)!")
                case 2:
                    print("Has seleccionado papel")
                    print("CPU ha seleccionado papel")
                    print("Es un empate :|")
                case 3:
                    print("Has seleccionado papel")
                    print("CPU ha seleccionado tijeras")
                    print("Has perdido  :(")
        case 3:
            match cpuPick:
                case 1:
                    print("Has seleccionado tijeras")
                    print("CPU ha seleccionado piedra")
                    print("Has perdido :(")
                case 2:
                    print("Has seleccionado tijeras")
                    print("CPU ha seleccionado papel")
                    print("Has ganado :)!")
                case 3:
                    print("Has seleccionado tijeras")
                    print("CPU ha seleccionado tijeras")
                    print("Es un empate :|")


jugar(userInput)
