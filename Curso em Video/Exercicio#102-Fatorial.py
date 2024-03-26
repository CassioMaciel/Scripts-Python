"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros. O
primeiro indica o número que será feito o fatorial, e o outro chamado show,
que será o valor lógico (opcional) indicando se será mostrado ou não na tela de
processo o cálculo do fatorial

Fonte:https://www.youtube.com/watch?v=84jUX96cs7Q
"""


def fatorial(n: int, show=False) -> int:
    """

    fatorial(n, show=False):
        -> calcula o fatorial de um número
        :param n: Número a ser calculado o fatorial
        :param show: valor lógico opcional indicando se será mostrado ou não o
        cálculo do fatorial
        :return: O valor do fatorial de n
    """
    produto = 1
    return_var = ""
    for index in range(n, 1, -1):
        produto = produto * index
        if show:
            return_var = return_var + f' {index} x'
    if show:
        return_var = return_var + f' 1 = {produto}'
    else:
        return_var = produto
    return return_var


if __name__ == '__main__':
    # help(fatorial)
    print(fatorial(5, show=False))
