################## Enunciado ###############################################
#	Faça um programa que leia o cateto oposto e o cateto adjacente de uma 
#	triangulo retangulo e mostre o comprimento da hipotenusa
############################################################################
import math
Cateto1=float(input('Digite o cateto oposto \n'))
Cateto2=float(input('Digite o cateto adjacente \n'))
print('O triangulo retangulo com cateto oposto {} e cateto adjacente {} tem a hipotenusa de {}'.format(Cateto1,Cateto2,math.sqrt(math.pow(Cateto1,2)+math.pow(Cateto2,2))))
