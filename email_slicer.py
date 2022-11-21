email = input("Ingresa tu email: ")
domain = email[email.index("@")+1:]
match domain:
    case "gmail.com":
        print("Tu email es de gmail")
    case "hotmail.com":
        print("Tu email es de hotmail")
    case "yahoo.com":
        print("Tu email es de yahoo")
    case _:
        print("Tu email es personalizado, interesante ")