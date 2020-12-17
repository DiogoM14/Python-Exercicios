n1 = float(input('Qual é a tua nota? '))
n2 = float(input('Qual é a tua nota? '))
m = (n1+n2)/2
if m < 7:
    print('Estás \033[31mreprovado\033[m! A tua média é \033[34m{}\033[m'.format(m))
elif m >= 7 and m <= 9.4:
    print('Tens de ir a \033[33mrecuperação\033[m! A tua média é \033[34m{}\033[m'.format(m))
else:
    print('Estás aprovado. \033[33mParabéns\033[m! A tua média é \033[34m{}\033[m'.format(m))