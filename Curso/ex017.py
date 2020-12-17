from math import hypot
c = float(input('Introduza o valor de um cateto: '))
cc = float(input('Introduza o valor de outro cateto: '))
s = hypot(c, cc)
print('O valor da sua hipotenusa é de {:.2f}!'.format(s))
