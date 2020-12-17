idade = int(input('Qual é a tua idade? '))
if idade == '18':
    print('Está na hora de ires à inspeção!')
elif idade < 18:
    n = 18 - idade
    print('Faltam {} anos para ires para a inspeção!'.format(n))
else:
    n2 = idade - 18
    print('Já foste à inspeção há {} anos!'.format(n2))
