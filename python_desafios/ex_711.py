altura=float(input('Qual é a altura da parede em m?'))
largura=float(input('Qual é a largura da parede em m'))
area=altura*largura
tinta_m=0.5
quantidade_tinta=area*tinta_m
print('A area da parede é de {} m2 '.format(area))
print('Necessita de  {} litros de tinta para pintar a parede'.format(quantidade_tinta))