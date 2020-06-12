
nome=str(input('Qual é seu nome?')).strip()
#nome=' Nuno Filipe Dos Santos Palhinhas Mota'

print(nome.upper())

print(nome.lower())

dividido=nome.split()

#soma=int(len(dividido[0]))+int(len(dividido[1]))+int(len(dividido[2]))+int(len(dividido[3]))+int(len(dividido[4]))+int(len(dividido[5]))
#print(soma)
print('O seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#len_Nome=len(dividido[0])

#print(len_Nome)

print('O seu 1º nome tem {} letras'.format(nome.find(' ')))