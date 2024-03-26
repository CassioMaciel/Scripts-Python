"""
Esse exercício busca saber como converter metros em suas dĩvisões
com objetivo educacional

Cassio Maciel - V0.1
Fonte: https://www.youtube.com/watch?v=KjcdG05EAZc
"""


entrada=float(input('Por favor digite uma distância em metros:\n'))

print('Uma medida de {} metros corresponde a:'.format(entrada))
print('{} km'.format(entrada/1000))
print('{} hm'.format(entrada/100))
print('{} dam'.format(entrada/10))
print('{} dm'.format(entrada*10))
print('{} cm'.format(entrada*100))
print('{} mm'.format(entrada*1000))