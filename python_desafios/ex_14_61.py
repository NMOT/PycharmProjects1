# Refazer o exercico 51 com o while

# n=int(input('Introduza o 1º termo da progressão aritmética.'))
# r=int(input('Introduza a razão da progressão '))
#
# for i in range(n,n+10): # Calcula os 10 primeiros termos de uma progressão aritmética
#
#     print(n+(i-1)*r)
#

i = 1
n = int(input('Introduza o 1º termo da progressão aritmética.'))
r = int(input('Introduza a razão da progressão '))

while i <= 10:
    print(n + (i - 1) * r)
    i += 1
