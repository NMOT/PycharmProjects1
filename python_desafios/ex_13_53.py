string =str(input('Que frase quer testar?'))
stringSemEspacos = string.replace(' ', '')
stringTodaMinuscula = stringSemEspacos.lower()
stringInvertida = stringTodaMinuscula[::-1]

if stringInvertida == stringTodaMinuscula:
    print("SIM")
else:
    print("NAO")