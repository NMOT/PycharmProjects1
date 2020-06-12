
s=0
t=0

for c in range(0,6):
    n=int(input('Digite um número.'))

    if n%2==0:

        s+=n
        t+=1

print('A soma dos números {} pares que digitou é {}'.format(t,s))