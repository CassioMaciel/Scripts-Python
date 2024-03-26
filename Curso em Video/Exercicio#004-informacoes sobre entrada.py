"""
Faça um programa que leia algo pelo teclado e mostre na tela todas as
informações possíveis sobre ele

Fonte: https://www.youtube.com/watch?v=tHYxjJxtJko&index=4
"""

entrada = input('Digite Qualquer coisa')

print('O tipo primitivo deste valor é',type(entrada))

print('Só tem espaços ?',entrada.isspace())

print('É um numero ?',entrada.isnumeric())

print('É alfabetico ?',entrada.isalpha())

print('É Alfanumerico ?',entrada.isalnum())

print('Está em maiusculas ?',entrada.isupper())

print('Está em minusculas',entrada.islower())

print('Está Captalizada ?',entrada.istitle())