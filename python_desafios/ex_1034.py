sal = float(input('Qual é o seu salário € ?'))
aum1 = 0.1
aum2 = 0.15


if sal > 1250:
    novo = sal + sal * aum1
else:
    novo = sal + sal * aum2
print('O seu salário passa de {}€ para {}€'.format(sal,novo))
