from datetime import datetime

maiores_idade = 0
menores_idade = 0
for i in range(0, 3):
    ano_nascimento = int(input('Qual é o ano de nascimento do {}º individuo ?'.format(i + 1)))
    if ano_nascimento < datetime.now().year:

        if datetime.now().year - ano_nascimento < 18:
            maiores_idade += 1
        else:
            menores_idade += 1

    else:

        print('Data de nascimento introduzida para o {}º elemento não é válida.'.format(i+1))

print('Neste grupo temos {} elementos maiores de idade e {} elementos que ainda não atingiram a maioridade.'.format(
    maiores_idade, menores_idade))
