text = input(
    "Ingresa el nombre de una organizacion o concepto para crearle un acronimo: ")
text = text.split(" ")
acronym = ""
for word in text:
    acronym += word[0].upper()
print(f"El acronimo es: {acronym} ")
