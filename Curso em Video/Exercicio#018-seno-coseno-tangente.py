"""
#################	Enunciado ################################################
Faça um programa que leia um angulo qualquer e informe o valor do seno,
do cosseno e da tangente

Fonte: https://www.youtube.com/watch?v=9GvsphwW26k
##############################################################################
"""
from math import sin, pi, cos, tan
angulo = float(input('digite um angulo \n'))
print('o angulo {} tem seno de {:.3f} cosseno de {:.3f} e tangente de {:.3f}'
      .format(angulo,
              sin(angulo*pi/180),
              cos(angulo*pi/180),
              tan(angulo*pi/180)))
