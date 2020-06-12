def nif_valido(nif):
    return not sum((10 - i) * int(n) for i, n in enumerate(nif, 1)) % 11 % 10

n = 0

for i in range (100000000, 999999999):
    nif=i

    if nif_valido:
        print(i)
        n+=1

print('Calculou {} números de contribuinte'.format(n))