from random import randint
from time import sleep
ran = randint(0, 5)

print('-=-' *20)
print('Vou pensar em um número de 0 a 5, tente adivinhar! ')
print('-=-' *20)

n = int(input('\nEm que número pensei? '))

print('PROCESSANDO...')

sleep(2)

if n == ran:
    print('Boa! Tu ganhaste!')
else:
    print('Eu ganhei!!! O número que pensei foi {} não {}!'.format(ran, n))

