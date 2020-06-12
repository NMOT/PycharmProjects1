numero_converter=int(input('Introduza o número inteiro que quer converter!'))
base_conversao=str(input('''Digite:
                            1- Binário
                            2- Octal
                            3- Hexadecimal
                            '''))
if base_conversao=='1':
    print(bin(numero_converter))
elif base_conversao=='2':
    print(oct(numero_converter))
else:
    print(hex(numero_converter))
