preco = float(input('Qual é o preço do produto que quer comprar?'))

print('''Escolha a forma de pagamento.

1- Pronto Pagamento Cheque ou Dinheiro

2- Pagamento no Cartão de desconto

3- Em 2 prestações

4- Em 3 ou mais prestações''')

opccao = input()

if opccao == '1':

    print('Você terá 10% de desconto e o valor a pagar é {}€'.format(preco - preco * (10 / 100)))

elif opccao == '2':

    print('Você terá 5% de desconto e o valor a pagar é {}€'.format(preco - preco * (5 / 100)))

elif opccao == '3':

    print('Você não terá desconto e o valor a pagar é {}€'.format(preco))

elif opccao == '4':

    print('Você irá ter um agravamento de 20% e irá pagar {}€'.format(preco + preco * (20 / 100)))

else:

    print('Opcção não comtemplada.')
