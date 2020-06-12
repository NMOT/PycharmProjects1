tar1=0.5
tar2=0.45
dis=float(input('A sua viagem é de quantos km?'))

if dis<=200:
    print('As portagens vão custar {}€'.format(dis*tar1))
else:
    print('As portagens vão custar {}€'.format(dis*tar2))