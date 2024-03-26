"""
Reescreva a função leia int que fizemos no desafio 104, incluindo agora a
possibilidade de digitação de um número invalido
aproveite e escreva tambem a função leia float com a mesma funcionalidade
"""


def leia_int():
    stay = True
    while stay:
        try:
            integer = int(input('por favor digite um inteiro: '))
        except (ValueError, TypeError):
            print('Por favor digite um número do tipo INTEIRO')
            continue
        except KeyboardInterrupt:
            print(f'Entrada de dados interrompida pelo usuário.')
            break
        else:
            return integer


def main():
    integer = leia_int()
    print(f'o valor digitado foi {integer}')


if __name__ == '__main__':
    main()
