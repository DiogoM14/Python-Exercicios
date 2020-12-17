from random import choice

msg = str(input('Qual o 1 aluno? '))
msg2 = str(input('Qual o 2 aluno? '))
msg3 = str(input('Qual o 3 aluno? '))
msg4 = str(input('Qual o 4 aluno? '))

lista = [msg, msg2, msg3, msg4]

r = choice(lista)

print('O aluno escolhido foi o/a {}!'.format(r))