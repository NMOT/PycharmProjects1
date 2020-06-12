import random

c = 0
numAl = int(random.randint(0, 10))
while True:
    c += 1
    numUtil = int(input('Digite um número entre 0 e 10.'))

    if numAl == numUtil:
        print('Parabéns acertou! Depois de {}º tentativas'.format(c))
        break
    else:
        print('É pena mas errou! Tente outra vez.')

