r1 = int(input('Introduza o comprimento da 1ª recta.'))
r2 = int(input('Introduza o comprimento da 2ª recta.'))
r3 = int(input('Introduza o comprimento da 3ª recta.'))
if r2 + r3 > r1 > abs(r2 - r3):
    print('É possível construir um triângulo', end=' ')

    if r1 == r2 == r3:

        print('Equilátero')

    elif r1 != r2 != r3 != r1:

        print('Escaleno')

    else:

        print('Isósceles')


else:
    print('Não é possível construir um triângulo com estas rectas.')
