from datetime import date

ano_nascimento = int(input('ANO DE NASCIMENTO?'))

idade = date.today().year-ano_nascimento

if idade <= 9:

    print('Você vai competir em: INFANTIS ')

elif 9 < idade <= 14:

    print('Você vai competir em: INICIADOS')

elif 14 < idade <= 19:

    print('Você vai competir em: JUNIORES')

elif 19 < idade <= 20:

    print('Você vai competir em: SENIORES')

else:

    print('Você vai competir em: MASTERS')
