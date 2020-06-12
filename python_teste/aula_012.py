nome = str(input('Qual é o seu nome?')).strip().upper()

if nome == 'NUNO':

    print('Que nome bonito!')
elif nome == 'MARIA' or nome == 'JOSE' or nome == 'PAULO':

    print('Seu nome é muito popular em Portugal.')

elif nome in 'Sofia Susana Catarina Iris'.strip().upper():

    print('Belo nome feminino!')

else:

    print('Seu nome é muito vulgar!')

print('Tenha um bom dia, {}!'.format(nome))
