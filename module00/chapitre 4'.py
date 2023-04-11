# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:21:17 2023

@author: Quetsia
"""


A=None
B=None
for i in range(2):
     while True:
         user_input=input(f"Entrer le nombre entier {i+1}:")
         try:
             val=int(user_input)
             if i==0:
                A=val
             else:
                B=val
             print(f"Vous avez entrer:",val)
             while B==0:
                 B=int(input("Entrer une valeur différente de 0:"))
             break
         except ValueError:
            print("Ce n'est pas un nombre entier.")
print("Somme=",A+B)
print("Différence=",A-B)
print("Produit=",A*B)
print("Quotient=",A/B)
print("Reste=",A%B)