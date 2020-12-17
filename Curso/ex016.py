from math import trunc

msg = float(input('Escreva um número para saber a sua porção inteira: '))
n = trunc(msg)
print('A parte inteira do número {} é {}'.format(msg, n))
