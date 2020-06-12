
# Permita que o usuário escolha quantos termos da progressão quer mostrar

#saia do programa quando o usuário disser que quer calcular mais 0 termos





i = 1

n = int(input('Introduza o 1º termo da progressão aritmética.'))
r = int(input('Introduza a razão da progressão '))
f = int(input('Quantos termos da progressão quer calcular?'))
while i < f+1:
    print(n + (i - 1) * r)
    i += 1
