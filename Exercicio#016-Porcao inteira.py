####################	ENUNCIADO##############################################
# crie um programa que leia um numero e retorne a porção inteira deste numero
# por exemplo, caso leia 6.127 escreva
# O numero 6.127 tem a parte inteira 6.
#
###############################################################################
import math
nota1=float(input('Digite o numero que você gostaria da porção inteira \n'))
print('O numero {} tem a parte inteira {}'.format(nota1,math.trunc(nota1)))
