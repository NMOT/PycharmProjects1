
"""
num=int(input('Digite um nº entre 0 e 9999.'))
n=str(num)
print('Analisando o número {}'.format(num))

print('Unidades: {}'.format(n[3]))
print('Dezenas: {}'.format(n[2]))
print('Centenas: {}'.format(n[1]))
print('Milhares: {}'.format(n[0]))  """


num=int(input('Digite um nº entre 0 e 9999.'))

print('Analisando o número {}'.format(num))

u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhares: {}'.format(m))

