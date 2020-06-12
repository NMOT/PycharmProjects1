vel=int(input('Introduza a velocidade a que circulava o carro em km/h? '))
unitario_multa=7

if vel>=80:
    print('''Circulava em excesso de velocidade.
             Uma vez que excedia a velocidade permitida em {}km/h.
             O valor da multa é {}'''
          .format(vel-80,(vel-80)*unitario_multa))
else:
    print('Parabéns.\nCirculava dentro dos limites legais')