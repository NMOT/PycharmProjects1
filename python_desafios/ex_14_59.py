c = 'S'
resultado = ''
print('****Rotina de Cálculo****')
print()

while c == 'S':
    n1 = int(input('Introduza o 1º valor.'))
    n2 = int(input('Introduza o 2º valor.'))
    print('\tQue operação pretende executar.\n\tEscolha uma das seguintes opcções.')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] exit')

    calculo = str(input())

    if calculo == '1':
        resultado = n1 + n2

    elif calculo == '2':
        resultado = n1 * n2

    elif calculo == '3':
        if n1 > n2:
            resultado = n1
        elif n1 == n2:
            resultado = 'Os números são iguais.'
        else:
            resultado = n2

    elif calculo == '4':

        c = 'S'

    else:
        break

    print(resultado)
