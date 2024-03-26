"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma linha de ^ em cima e em baixo de
tamanho adaptável
"""

def escreva(msg:str) -> None:
    tamanho = len(msg)
    print('~'*(tamanho+4))
    print(f'  {msg}')
    print('~'*(tamanho+4))


if __name__ == '__main__':
    escreva('cabeção')
    escreva('oi')
    escreva('jardim do edem')