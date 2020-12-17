n = str(input('Qual é o seu nome? '))
if n == 'Diogo':
    print('Que nome bonito!')
elif n == 'Paulo' or n == 'Maria' or n == 'Beatriz':
    print('O teu nome é bem popular!')
elif n in 'Ana Claudia Jéssica Juliana': # <------------------------------------------------
    print('Que nome bem feminimo')
else:
    print('O teu nome é muito normal!')
print('Tenha um bom dia, {}!'.format(n))