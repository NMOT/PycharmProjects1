#Lê vários números pelo teclado, pergunta ao utilizador se quer continuar.
#No final apresenta a média, o maior e o menor.
s = m = i = M = p =0
r = 'S'
while r in 'Ss':
    n = int(input('Digite um número: '))

    i += 1
    s += n

    if i == 1:
        M = p = n
    else:
        if n < p:
            p = n
        if n > M:
            M = n
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
m = s/i
print('A média aritmética dos números introduzidos é {} o máximo é {} e o mínimo é {}'.format(m,M,p))