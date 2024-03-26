"""
Faça um programa que tenha uma função chamada area(), que receba as
dimensões de um terreno retangular (largura e comprimento) e mostre a area
do terreno.
"""


def area(largura: float, comprimento: float) -> None:
    area_total = largura * comprimento
    print(f'A área de um terreno de {largura} x {comprimento} é de '
          f'{area_total} m²')


def main():
    print('-' * 79)
    print('|', end="")
    titulo = 'Controle de Terrenos'
    print(f'{titulo:^77}', end="")
    print('|')
    print('-' * 79)
    largura = float(input('Largura (m): '))
    comprimento = float(input('Comprimento (m): '))
    area(largura, comprimento)


if __name__ == '__main__':
    main()
