from datetime import date

atual = date.today().year
nascimento = int(input('Em que ano nasceste? '))
idade = atual-nascimento

if idade <= 9:
    print('A a tua categoria é MIRIM, pois tens {} anos!'.format(idade))
elif idade > 10 and idade <= 14:
    print('A a tua categoria é INFANTIL, pois tens {} anos!'.format(idade))
elif idade > 15 and idade <= 19:
    print('A a tua categoria é JUNIOR, pois tens {} anos!'.format(idade))
elif idade > 20 and idade <= 25:
    print('A a tua categoria é SÉNIOR, pois tens {} anos!'.format(idade))
else:
    print('A a tua categoria é MASTER, pois tens {} anos!'.format(idade))