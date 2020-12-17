f = str(input('Escreve uma frase: ')).strip().upper()
print('A letras "A" apareceu {} vezes na frase'.format(f.count('A')))
print('A letra "A" apareceu na posição {}'.format(f.find('A')+1))
print('A ultima letra "A" apareceu na posição {}'.format(f.rfind('A')+1))