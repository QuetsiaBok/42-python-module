# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:48:16 2023

@author: Quetsia
"""


print("Ceci est un jeu de devinettes interactif!")
print("   Vous devez entrer un nombre compris entre 0 et 100 pour connaître le numéro mystère")
print("      Tapez 'exit' pour quitter le jeu.")
print("            BONNE  CHANCE")
import random
n=random.randint(0,100)
nbres_essais=5
while nbres_essais>0:
    nbres_essais -=1
    var=int(input("Quel est le nombre mystère?:"))
    if var<n:
        print("Le nombre mystère est plus grand!")
    elif var>n:
        print("Le nombre mystère est plus petit!")
    else:
        break
if nbres_essais !=0:
     print("Youpi!Vous avez trouvé le nombre mystère", var,"en",5-nbres_essais,"essais")
else:
    print("Oups! Vous avez dépassé le nombre d'essais.Le nombre mystère était",n,"Retentez votre chance")
    
    
    
    