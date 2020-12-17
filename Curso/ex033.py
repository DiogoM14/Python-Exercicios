'''n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

f = n1 - n2

if f < 1:
    print('O número maior é {}'.format(n2))
    print('O número menor é {} '.format(n1))
else:
    print('O número menor é {}'.format(n2))
    print('O número maior é {} '.format(n1))'''

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

menor = n1

if n2 < menor and n2 < n3:
    menor=n2

if n3 < n1 and n3 < n2:
    menor=n3

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))





