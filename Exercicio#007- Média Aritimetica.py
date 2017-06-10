#Exercicio que calcula a média aritimetica entre 2 notas do aluno e os mostra com formatação de casas decimais.#

nota1=float(input('Primeira nota do aluno:\n'))
nota2=float(input('Segunda nota do aluno:\n'))
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1,nota2,(nota1+nota2)/2))