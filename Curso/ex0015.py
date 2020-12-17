d = int(input('Por quantos dias alugou o carro? '))
k = float(input('Qunatos KM viajaste? '))
c = d*60+(k*0.15)
print('O total a pagar é de: {:.2f}$!'.format(c))