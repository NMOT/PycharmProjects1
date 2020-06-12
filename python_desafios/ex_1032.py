import _datetime

ano=int(input('Que ano quer analisar? Coloque 0 para analisar o ano actual.'))
if ano==0:
    ano=_datetime.date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ano de {} é BISEXTO.'.format(ano))
else:
    print('O ano de {} NÃO É BISEXTO.'.format(ano))