
r1 = int(input('Introduza o comprimento da 1ª recta.'))
r2 = int(input('Introduza o comprimento da 2ª recta.'))
r3 = int(input('Introduza o comprimento da 3ª recta.'))

if r2 + r3 > r1 > abs(r2 - r3):
    print('É possível construir um triângulo com estas rectas')
else:
    print('Não é possível construir um triângulo com estas rectas.')
