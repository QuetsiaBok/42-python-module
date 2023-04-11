# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:26:49 2023

@author: Quetsia
"""


chaine=input("Entrer une phrase:")
print("votre phrase est:",chaine)
"""inv=""
for i in range(len(chaine)-1,-1,-1):
    print(chaine[i])
    inv=inv+chaine[i]
    print(inv)"""
inv=chaine[::-1]
print(inv)
print(chaine.swapcase())
