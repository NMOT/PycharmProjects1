
while True:
    n = str(input('Qual é o seu sexo?').upper())

    if n in 'M,F':
        break
    else:
        c = 0
        print('Valor digitado inválido.')
        print('Valores admitidos M/F.')