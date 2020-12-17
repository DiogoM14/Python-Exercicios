l1 = float(input('Qual é o comprimento do primeiro lado? '))
l2 = float(input('Qual é o comprimento do segundo lado? '))
l3 = float(input('Qual é o comprimento do terceiro lado? '))
if l1 < l2 + l3 and l2 < l1 + l3 < l3 or l3 < l1 + l2:
    print('É possivel criar um triângulo!')
    if l1 == l2 == l3:
        print('O triângulo formado é EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        print('O triângulo é ESCALENO!')
    else:
        print('O triângulo formado é ISÓSCELES!')
else:
    print('Não é possivel formar um triângulo! ')