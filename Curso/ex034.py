s = float(input('Quanto é o teu salário? '))
if s <= 700:
    st = s * 0.15
else:
    st = s*0.10
sf = s + st
print('O seu salário passou de {} para {}'.format(s, sf))