#Faça um programa que leia algo pelo teclado e mostre na tela todas as informações possiveis sobre ele

#https://www.youtube.com/watch?v=hdDHg1p3YVc&index=7&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6    minuto 26:46

#resposta: https://www.youtube.com/watch?v=tHYxjJxtJko&index=4&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-

entrada = input('Digite Qualquer coisa')

print('O tipo primitivo deste valor é',type(entrada))

print('Só tem espaços ?',entrada.isspace())

print('É um numero ?',entrada.isnumeric())

print('É alfabetico ?',entrada.isalpha())

print('É Alfanumerico ?',entrada.isalnum())

print('Está em maiusculas ?',entrada.isupper())

print('Está em minusculas',entrada.islower())

print('Está Captalizada ?',entrada.istitle())