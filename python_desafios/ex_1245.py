import random

print('Bem Vindo ao Jokenpô')

print('''1 - Pedra
2 - Papel
3 - Tesoura ''')

jogada_humana = int(input())

jogada_computador = int(random.randint(1, 3))


if jogada_humana == 1:

    if jogada_computador == 1:

        print('Computador jogou "Pedra": EMPATE')

    elif jogada_computador == 2:

        print('Computador jogou "Papel": COMPUTADOR GANHOU')

    else:

        print('Computador jogou "Tesoura": VOCÊ GANHOU')

elif jogada_humana == 2:

    if jogada_computador == 1:

        print('Computador jogou "Pedra": VOCÊ GANHOU')

    elif jogada_computador == 2:

        print('Computador jogou "Papel": EMPATE')

    else:

        print('Computador jogou "Tesoura": COMPUTADOR GANHOU')

elif jogada_humana == 3:

    if jogada_computador == 1:

        print('Computador jogou "PEDRA": COMPUTADOR GANHOU')

    elif jogada_computador == 2:

        print('Computador jogou "PAPEL": VOCÊ GANHOU')

    else:

        print('Computador jogou "TESOURA": EMPATE')

else:

    print('Opcção inválida')
