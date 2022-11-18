print("Bienvenido a mad libs!\n" +
      "cuenta una historia con tus propias palabras\n")
animal = input("Escribe un animal:")
nombre = input("Dale un nombre al animal que escribiste:")
verbo = input("Escribe un verbo:")


def print_mad_lib(animal, nombre, verbo):
    print("")
    print(f"Habia una vez un {animal}")
    print(f"que se llamaba {nombre}")
    print(f"y le gustaba {verbo}")


print_mad_lib(animal, nombre, verbo)
