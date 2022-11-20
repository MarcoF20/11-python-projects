import re

name = input("Ingresa tu nombre: ")

while name.isalpha() == False:
    print("Formato invalido, escribe solo letras\n")
    name = input("Ingresa tu nombre: ")


birthday = input("Ingresa tu fecha de nacimiento (mm/dd/yyyy): ")
mo = re.compile("\d\d/\d\d/\d\d\d\d").search(birthday)
while mo == None:
    print("Formato invalido, escribe la fecha de la siguiente manera: mm/dd/yyyy\n")
    birthday = input("Ingresa tu fecha de nacimiento (mm/dd/yyyy): ")
    mo = re.compile("\d\d/\d\d/\d\d\d\d").search(birthday)
birthday = mo.group()

address = input("Ingresa tu domicilio: ")
goals = input("Escribe una meta personal que tengas: ")

print(f"""
Nombre: {name}
Fecha de nacimiento: {birthday}
Domicilio: {address}
Meta personal: {goals}""")
