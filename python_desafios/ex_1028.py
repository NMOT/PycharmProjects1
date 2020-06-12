import random

numAl = int(random.randint(0, 5))
print(numAl)
numUtil = int(input('Digite um número entre 0 e 5.'))

if numAl == numUtil:
    print('Parabéns acertou!')
else:
    print('É pena mas errou!')
