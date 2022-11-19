print("Bienvenido a mad libs!\n" +
      "cuenta una historia con tus propias palabras\n")
animal = input("Escribe un animal:")
name = input("Dale un nombre al animal que escribiste:")
verb = input("Escribe un verbo:")


def print_mad_lib(animal, name, verb):
    print("")
    print(f"Habia una vez un/a {animal}")
    print(f"que se llamaba {name}")
    print(f"y le gustaba {verb}")


print_mad_lib(animal, name, verb)
