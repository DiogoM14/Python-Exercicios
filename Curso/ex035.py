l1 = float(input('Qual a medida do primeiro lado? '))
l2 = float(input('Qual a medida do segundo lado? '))
l3 = float(input('Qual é a medida do terceiro lado? '))

if l1 < l2 + l3 and l2 < l1 + l3 < l3 or l3 < l1 + l2:
    print('É possivel forma um triângulo!')
else:
    print('É impossivel formar um triângulo!')