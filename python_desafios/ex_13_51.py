n=int(input('Introduza o 1º termo da progressão aritmética.'))
r=int(input('Introduza a razão da progressão '))

for i in range(n,n+10): # Calcula os 10 primeiros termos de uma progressão aritmética

    print(n+(i-1)*r)