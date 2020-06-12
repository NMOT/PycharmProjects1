# S = ('Fome')
# C = ('Merda', 'Fome', 'Parto')
# if S in C :
#     print(True)
# else:
#     print(False)
#
#
# 020314350   607080 -  FAR. GRANEL
# 1020314450   607182 - FAR. SACO 30 kg.
# 1020314650   617080 - GRAN. GRANEL

A1 = 'GRAN.GRANEL617080'
B1 = 'FAR.SACO607182'
C1 = 'GRAN.SACO617182'

h1 = '617182'
d1 = 'GRAN.SACO'

if h1 in A1 and d1 in A1:
    print('Ok')
elif h1 in B1 and d1 in B1:
    print('Ok')
elif h1 in C1 and d1 in C1:
    print('Ok')
else:
    print('Not Ok')
