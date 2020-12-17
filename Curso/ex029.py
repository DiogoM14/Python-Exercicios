v = float(input('Qual é a velocidade atual do carro? '))
if v <= 80:
    print('\nEstá dentro do limite de velocidade!'
          '\nTenha um bom dia e conduza com cuidado!')
else:
    multa = (v-80) * 3
    print("\nMULTADO! Excedeu o limite de velocidade que é 80Km/h"
          "\nTem de pagar uma multa de {:.2f}$!"
          "\nTenha um bom dia e conduza com segurança!".format(multa))