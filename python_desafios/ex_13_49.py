n=int(input('De que número quer calcular a tabuada?'))

for c in range(1,11):

    m = c*n
    print('{:2} x {:2} = {:2}'.format(n,c,m))