"""
##########################	Enunciado #########################################
O professor tem 4 alunos, faça um programa que leia o nome deles e sorteie
a ordem de apresentação deles

Fonte: https://www.youtube.com/watch?v=OPh0nngbBSY
###############################################################################
"""
from random import sample
Aluno1 = input('Digite o nome do aluno 1 \n')
Aluno2 = input('Digite o nome do aluno 2 \n')
Aluno3 = input('Digite o nome do aluno 3 \n')
Aluno4 = input('Digite o nome do aluno 4 \n')
vetorSaida = sample([Aluno1, Aluno2, Aluno3, Aluno4], 4)
print('\nO primeiro será o {}\n'
      ' O segundo será o {}\n'
      ' O terceiro será {}\n'
      ' O quarto será {}'.format(vetorSaida[0],
                                 vetorSaida[1],
                                 vetorSaida[2],
                                 vetorSaida[3]))
