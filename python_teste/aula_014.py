# for c in range(1, 10):
#     print(c)
#  print('Fim')



# b = 1
# while b < 10:
#     print(b)
#     b += 1
# print('Fim')
#
# n = 1
# par = impar = 0
# while n != 0:
#     n = int(input('Digite um valor: '))
#     if n!=0:
#         if n % 2 == 0:
#             par += 1
#         else:
#             impar += 1
# print('Terminou!')
# print('Digitou {} números'.format(par + impar))
# print('Dos números digitados {} são pares.'.format(par))
# print('Dos números digitados {} são impares. '.format(impar))


c = 0
while c == 0:
    n = str(input('Qual é o seu sexo?').upper())

    if n in 'M,F':
        c = 1
    else:
        c = 0
        print('Valor digitado inválido.')
        print('Valores admitidos M/F.')
