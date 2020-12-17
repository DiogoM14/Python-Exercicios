n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = ((n1+n2)/2)
if m >= 10:
    print('Passa-te com média de {}'.format(m))
else:
    print('Reprovas-te com média de {}'.format(m))