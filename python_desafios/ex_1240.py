nota1 = float(input('Introduza a nota da 1ª disciplina'))
nota2 = float(input('Introduza a nota da 2ª disciplina'))
media = (nota1 + nota2) / 2

if media < 5:

    print('Média abaixo de 5.0: REPROVADO')

elif 5 < media < 6.9:

    print('Média entre 5.0 e 6.9: EM RECUPERAÇÂO')

else:

    print('Média de 7.0 ou superior: APROVADO')
