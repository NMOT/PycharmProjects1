from random import choice



n1=str(input('Digite o nome do 1º aluno.'))
n2=str(input('Digite o nome do 2º aluno.'))
n3=str(input('Digite o nome do 3º aluno.'))
n4=str(input('Digite o nome do 4º aluno.'))
Lista=[n1, n2, n3, n4]
escolhido= choice(Lista)

print('O aluno {} foi escolhido para apagar o quadro'.format(escolhido))

