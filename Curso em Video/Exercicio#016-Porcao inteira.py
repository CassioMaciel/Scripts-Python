"""
####################	ENUNCIADO #############################################
crie um programa que leia um número e retorne a porção inteira deste número,
por exemplo, caso leia 6.127 escreva
O número 6.127 tem a parte inteira 6.

Fonte: https://www.youtube.com/watch?v=-iSbDpl5Jhw
###############################################################################
"""
import math
nota1 = float(input('Digite o numero que você gostaria da porção inteira \n'))
print('O numero {} tem a parte inteira {}'.format(nota1, math.trunc(nota1)))
