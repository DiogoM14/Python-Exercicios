print('{:=^40}'.format(' Lojas Martins '))

preco = float(input('Qual é o preço original do produto? '))
print('''Qual é a forma que pretende efetuar o pagamento? 
      1 - Cheque/Dinhero 10% de desconto 
      2 - Cartão 5% de desconto 
      3 - 2xCartão 
      4 - 3xCartão 20% de juros  ''')

pag = int(input('Insira a sua escolha aqui: '))
if pag == 1:
    precof = preco - (preco * 0.1)
elif pag == 2:
     precof = preco - (preco * 0.05)
elif pag == 3:
    precof = preco
elif pag == 4:
     precof = preco + (preco * 0.2)
print('''O produto que escolheu ficará por um preço de {} euros. 
    Obrigado!'''.format(precof))