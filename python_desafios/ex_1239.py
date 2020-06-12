from datetime import date

print('Este programa informa qual o timing para você dar o nome para tropa.')
ano_nascimento = int(input('Ano Nascimento:'))

ano_actual = date.today().year
ano_alistamento = ano_nascimento + 18
idade = ano_actual - ano_nascimento

if idade>35:

    print('Você tem mais de 35 anos.')
    print('Você já está dispensado de se alistar')

elif idade < 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_actual))
    print('Ainda faltam {} anos para o alistamento.'.format(ano_alistamento - ano_actual))
    print('Seu alistamento será em {}'.format(ano_alistamento))

elif idade > 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento, idade, ano_actual))
    print('Você deveria ter-se alistado à {} anos.'.format(ano_actual-ano_alistamento))
    print('Seu alistamento foi em {}.'.format(ano_alistamento))

else:
    print('Voçê tem {} anos.'.format(idade))
    print('Você tem de se alistar IMEDIATAMENTE!')
    print('Seu ano de alistamento é {}'.format(ano_actual))
