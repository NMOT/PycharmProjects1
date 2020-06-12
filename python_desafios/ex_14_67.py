# Programa que cálcula a tabuada de vários números #
# De seguida mostra no ecrã os resultado, continua até ser digitado um número negativo #

n = 1

while True:
    n = int(input('Quer ver a tabuada de que valor? '))
    if n < 0:
        break
    print('-'*30)
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')

    print('-'*30)
print('PROGRAMA TABUADA ENCERRADA. ')




