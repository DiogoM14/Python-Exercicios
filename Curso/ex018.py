from math import tan, sin, cos, radians
an = float(input('Qual o ângulo que pretende saber? '))
t = tan(radians(an))
s = sin(radians(an))
c = cos(radians(an))

print('O ângulo de {} tem a tangente de {:.2f}. \nO ângulo de {} tem o seno de {:.2f}. \nO ângulo de {} tem o cosseno de {:.2f}.'.format(an, t, an, s, an, c))