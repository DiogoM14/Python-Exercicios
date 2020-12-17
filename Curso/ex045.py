from random import randint
from time import sleep
print('{:^45}'.format('{Bem Vindo ao jogo Pedra-Papel-Tesoura}\n'))

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

jogador = int(input('''Qual é a tua jogada? 
    [ 0 ] - Pedra 
    [ 1 ] - Papel 
    [ 2 ] - Tesoura? 
     == Jogada => '''))

print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')

print('-=' * 12)
print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('-=' * 12)

if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador Ganhou!')
    elif jogador == 2:
        print('Computador ganhou!')
    else:
        print('Jogada invalida!')

elif computador == 1:
    if jogador == 0:
        print('Computador ganhou!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador ganhou!')
    else:
        print('Jogada invalida!')

elif computador == 2:
    if jogador == 0:
        print('Jogador ganhou!')
    elif jogador == 1:
        print('Computador ganhou!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada invalida!')