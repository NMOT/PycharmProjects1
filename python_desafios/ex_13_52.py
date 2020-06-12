n = int(input('Introduza o número que quer verificar se é primo.'))

div = 0
for i in range(1, n+1):

    if n % i == 0:
        div +=1
if div == 2:

    print('O número {} é primo'.format(n))

else:

    print('Não é primo.')
