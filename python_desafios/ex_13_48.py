t = 0
s = 0
for c in range(0, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            s += c
            t += 1

print('Entre 0 e 500 existem {} números ímpares que são múltiplos de 3, e a sua soma é {}.'.format(t,s))
