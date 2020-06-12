# Soma de vários números
s = 0
n = 0
i = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]:'))
    if n == 999:
        break
    else:
        s += n
        i += 1
print('Você digitou {} números cuja soma é {}'.format(i, s))
