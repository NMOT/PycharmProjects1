euros_carteira=float(input('Que valor em € tem na carteira?'))
fator_conversão=1.19
dolares=euros_carteira*fator_conversão
print('Pode comprar {:6.2f} dólares!'.format(dolares))