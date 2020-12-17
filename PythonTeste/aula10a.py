#nome = str(input('Qual é o teu nome? '))
#s = nome.split()
#if s[0] == 'Diogo':
#    print('Tens um nome lindo!')
#else:
#    print('O teu nome é tão normal!')
#print('Bom dia, {}!'.format(s[0]))

n1 = float(input('Qual a sua primeira nota? '))
n2 = float(input('QUal a sua segunda nota? '))
m = (n1 + n2) / 2
print('A tua média é {:.1f}'.format(m))
if m <= 6.0:
    print('A tua média foi boa! Parabéns')
else:
    print('A tua média foi má! Tens de estudar mais.')
