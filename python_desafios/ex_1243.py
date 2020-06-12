print('******CÁLCULO MASSA CORPORAL******')

peso = float(input('Introduza o seu peso em kg:'))
altura = float(input('Introduza a sua altura em m:'))

imc = peso / altura ** 2

print('Classificação de IMC:', end=' ')
if imc < 18.8:

    print('SubPeso.')

elif 18.8 <= imc < 25:

    print('Peso Ideal.')

elif 25 <= imc < 30:

    print('Sobrepeso')

elif 30 <= imc < 40:

    print('Obeso')

else:

    print('Obesidade Mórbida')
