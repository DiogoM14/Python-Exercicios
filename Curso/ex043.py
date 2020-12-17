peso = float(input('Qual é o teu peso em KG? '))
altura = float(input('Qual é a tua altura? '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('O teu IMC é de {:.2f}, estás a \033[31mbaixo\033[m do peso!'.format(imc))
elif 18.5 <= imc < 25:
    print('O teu IMC é de {:.2f}, estás com o peso \033[38mideal\033[m!'.format(imc))
elif 25 <= imc < 30:
    print('O teu IMC é de {:.2f}, estás com  \033[31mexcesso de peso\033[m!'.format(imc))
elif 30 >= imc < 40:
    print('O teu IMC é de {:.2f}, estás com \033[31mobesidade\033[m!'.format(imc))
else:
    print('O teu IMC é de {:.2f}, estás com \033[31mobesidade morbida\033[m!'.format(imc))