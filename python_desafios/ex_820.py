import random

n1=str(input('Primeiro aluno: '))
n2=str(input('Segundo Nome: '))
n3=str(input('Terceiro nome: '))
n4=str(input('Quarto nome: '))
Lista=[n1, n2, n3, n4]
random.shuffle(Lista)
print('A ordem de apresentação dos trabalhos será {}'.format(Lista))
