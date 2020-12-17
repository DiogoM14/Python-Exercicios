num = int(input('Qual é o número que pretende converter? '))
print('''Escolha umas das bases para conversão!
[ 1 ] Conversão para Binário
[ 2 ] Conversão para Octadecimal
[ 3 ] Conversão para Hexadecimal
''')
opcao = int(input('Qual a tua opção? '))

if opcao == 1:
    print('O número {} em Binário é {}'.format(num, bin(num)))
if opcao == 2:
    print('O número {} em Binário é {}'.format(num, oct(num)))
if opcao == 3:
    print('O número {} em Binário é {}'.format(num, hex(num)))
else:
    print('Opção inválida! Tente novamente.')