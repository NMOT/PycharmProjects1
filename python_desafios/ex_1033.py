n1 = int(input('Introduza o 1º número.'))
n2 = int(input('Introduza o 2º número.'))
n3 = int(input('Introduza o 3º número.'))
if n1 > n2 and n1 > n3:
    maior = n1
if n1 < n2 and n1 < n2:
    menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n2 < n1 and n2 < n3:
    menor = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n3 < n1 and n3 < n2:
    menor = n3

print('O número {} é o MAIOR dos 3'.format(maior))
print('O número {} é o MENOR dos 3'.format(menor))
