# Lê vários números pelo teclado, pergunta ao utilizador se quer continuar e pará se o utilizador digitar 999.
# No final apresenta a soma dos valores digitados e quantos valores digitou.

r = ' '
n = c = soma = 0

while r not in '999':
    n = int(input('Digite um valor (999 para parar) :'))
    if n ==999:
        break
    else:
        c+=1
        soma+=n
print('Você digitou {} valores e a soma dos mesmos é {}'.format(c,soma))

