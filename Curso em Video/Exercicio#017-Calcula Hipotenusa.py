"""
##################### Enunciado ###############################################
Faça um programa que leia o cateto oposto e o cateto adjacente de uma
triangulo retângulo e mostre o comprimento da hipotenusa.

Fonte: https://www.youtube.com/watch?v=vmPW9iWsYkY
###############################################################################
"""
import math
cateto1 = float(input('Digite o cateto oposto \n'))
cateto2 = float(input('Digite o cateto adjacente \n'))
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print('O triangulo retângulo com cateto oposto {} e cateto adjacente {} tem a '
      'hipotenusa de {}'.format(cateto1, cateto2, hipotenusa))
