# -*- coding: utf-8 -*-
"""Punto_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyLPKr76XsXXICfinr2kBoVhA43Up0iB

# **Segundo Punto**

**Enunciado:** Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
"""

n = 1
Lista_impares=[]
Lista_pares=[]

while n <= 1000:
  if n%2==0:
    Lista_pares.append(n)
  else:
    Lista_impares.append(n)
  n += 1

print("Los números impares: " + str(Lista_impares))
print("Los números pares: " + str(Lista_pares))