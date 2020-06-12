n = int(input('Digite o número que quer calcular o factorial.'))

if n == 0:
    fatorial = 1
else:
    fatorial = 1
    while n > 0:
        fatorial *= n
        n -= 1

print('O fatorial de {} é {}'.format(n, fatorial))
