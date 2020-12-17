n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo valor: '))
if n1 == n2:
    print('Não existe valor maior, são os dois \033[36miguais\033[m! ')
elif n1 > n2:
    print('O \033[36mprimeiro\033[m valor é o maior!')
else:
    print('O \033[36msegundo\033[m valor é o maior! ')