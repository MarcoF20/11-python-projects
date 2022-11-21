text = input("Ingresa una palabra o frase y veamos sin es un palindromo: ")
textMin = text.lower()
textTrimmed = textMin.replace(" ", "")
if textTrimmed == textTrimmed[::-1]:
    print(f"{text} es un palindromo")
else:
    print(f"{text} no es un palindromo")