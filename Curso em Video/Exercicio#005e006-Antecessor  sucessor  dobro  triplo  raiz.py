"""
Exercício 005:
Faça um programa que leia um número inteiro e mostre na tela seu antecessor
e seu sucessor

Fonte:https://www.youtube.com/watch?v=664e0G_S9nU


Exercício 006:
Crie um algorítimo que leia um número e mostre seu dobro, triplo e raiz
quadrada

Fonte:https://www.youtube.com/watch?v=mqcNw_dhl8I
"""

valor = int(input("Digite um valor \n"))

print(f'Analisando o valor {valor}, vemos que:')
print(f'O antecessor é {valor-1}')
print(f'O sucessor é {valor+1}')
print('O dobro de {} é {}'.format(valor, valor*2))
print('O triplo de {} é {}'.format(valor, 3*valor))
print('O quadrado de {} é {}'.format(valor, valor**2))
print('A raiz quadrada de {} é {}'.format(valor, valor**(1/2)))
