#Sequência Fibonacci v 1.0

print('-'*30)
print('Sequência Fibonacci')
print('-'*30)
n = int(input('Quanto termos quer mostar? '))

t1 = 0
t2 = 1
print('~'*30)
print('{}\u2192{}'.format(t1,t2),end = '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('\u2192{}'.format(t3),end='')
    t1=t2
    t2=t3
    cont+=1
print('\u2192Fim',end='')