
frase=str(input('Digite uma frase.')).strip().lower()

print('A sua frase tem {} a letra a'.format(frase.count('a')))
print('A primeira ocorrência da letra a é na posição {}'.format(frase.find("a")+1))
print('A última ocorrência da letra ''a'' é na posição {}'.format(frase.rfind('a')+1))
