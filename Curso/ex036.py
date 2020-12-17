casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Pretende pagar a casa em quantos anos? '))

prestacao = casa/(anos * 12)
resto = salario-prestacao

if resto <= 0.30*salario:
    print('A prestação a pagar é de {:.2f} euros mensais!'.format(prestacao))
    print('O emprestimo foi \033[31mnegado\033[m!')
else:
    print('A prestação a pagar é de {:.2f} euros mensais!'.format(prestacao))
    print('O emprestimo foi \033[32maceite\033[m e terá de pagar {:.2f} por mês!'.format(prestacao))