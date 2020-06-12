salario_actual=float(input('Qual é o seu salário actual?'))
aumento_salario=float(input('Qual é a taxa de aumento?' ))/100
salario_novo=salario_actual+salario_actual*aumento_salario
print('O salário após o aumento será de {}€'.format(salario_novo))