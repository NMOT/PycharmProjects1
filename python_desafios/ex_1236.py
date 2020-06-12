print('Bem vindo!')
print('Vamos iniciar o processo para a avaliação da condição de concessão de crédito para a compra de uma casa.')
input('Carregue numa tecla para continuar')
valor_casa = float(input('Qual é o valor da casa que quer comprar?'))
salario = float(input('Quanto ganha por mês em valor liquído?'))
prazo_anos = int(input('Em quantos anos você quer pagar a casa?'))
prazo_meses = prazo_anos * 12
prestacao_mensal = valor_casa / prazo_meses

if prestacao_mensal <= salario * (30 / 100):

    print('O crédito foi aprovado!')

    print('A sua prestação mensal será de {:.2f}€'.format(prestacao_mensal))
else:

    print('''Lamentamos mas não é possível aprovar o crédito.
            A taxa de esforço é superior a 30% do seu salário.''')
