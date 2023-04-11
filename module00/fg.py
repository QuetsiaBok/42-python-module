nom = "toto"
print("je m'appelle", nom)
print("je suis",nom,"j'ai",30,"ans" )

nom1=input("le nom de la personne 1:")
age1=input("l'age de la personne 1:")
print("la personne 1 est",nom1 ,"son age est" ,age1, "ans")
print("le nom comporte",len(nom1), "lettres")


nom2=input("le nom de la personne 2:")
age2=input("l'age de la personne 2:")
print("la personne 2 est",nom2 ,"son age est" ,age2, "ans")
print("le nom comporte",len(nom2), "lettres")

nom3=input("le nom de la personne 3:")
age3=input("l'age de la personne 3:")
print("la personne 2 est",nom3 ,"son age est" ,age3, "ans")
print("le nom comporte",len(nom3), "lettres")

print("début du programme")
def afficher_info_personnelles():
     print("toto")
     print("titi")
afficher_info_personnelles()

print("fin du programme")

def afficher_info_personnelles(nom="" , age=0):
    if nom=="":
        print("vous n'avez entré aucunes informations")
        return

    if age==0:
        print("la personne est", nom)
    else:
           print("la personne est" ,nom, "son âge est",age)
           print("son nom comporte",len(nom), "caractères")
           print("Début du programme")
print("Fin du programme")
afficher_info_personnelles()