"""
###################	Enunciado #################################################
Um professor tem 4 alunos e quer sortear quem deles vai apagar o quadro
Faça um programa que leia o nome deles e informe quem vai apagar o quadro

Fonte: https://www.youtube.com/watch?v=_Nk02-mfB5I
###############################################################################
"""
from random import choice
Aluno1 = input('Digite o nome do aluno 1 \n')
Aluno2 = input('Digite o nome do aluno 2 \n')
Aluno3 = input('Digite o nome do aluno 3 \n')
Aluno4 = input('Digite o nome do aluno 4 \n')
print('\n{}'.format(choice([Aluno1, Aluno2, Aluno3, Aluno4])))
