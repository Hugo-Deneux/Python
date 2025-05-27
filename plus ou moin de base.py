import random

nombre = None
nb_choisie= None
rejouer = "yes"

while rejouer == "yes":
    nombre = random.randint(1,10)
    nb_choisie= None
    while nb_choisie != nombre:
        nb_choisie = int(input("nb?"))
        if nb_choisie < nombre:
            print("+")
        elif nb_choisie > nombre:
            print("-")
        else:
            print("good job")
    rejouer = input("rejouer yes or no ")


