    for c in range(7, 0, -1):
    print(c)

print('FIM')

for c in range(0, 7, 2):
    print(c)

print('FIM')

n = int(input('Escreva um número: '))
for c in range (0, n+1):
    print(c)

print('FIM')

i = int(input('INICIO: '))
s = int(input('SALTO: '))
f = int(input('FIM: '))
for c in range(i, f+1, s):
    print(c)

print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Escreva um número: '))
    s = s + n
print('A soma de todos os valores é de {}'.format(n))