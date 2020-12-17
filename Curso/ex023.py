num = int(input('Introduza um número entre 0 e 99999: '))
print('A analisar o número {}'.format(num))
n = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(n))
print('Dezena: {}' .format(d))
print('Centena: {}'.format(c))
print('Milhar: {}' .format(m))