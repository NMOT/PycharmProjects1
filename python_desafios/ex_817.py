
import math

cateto_adjacente=float(input('Qual é o comprimento do cateto adjacente em cm?'))
cateto_oposto=float(input('Qual é o comprimento do cateto oposto em cm?'))
hipotenusa=math.hypot(cateto_adjacente,cateto_oposto)
print('A hipotenusa é {}'. format(hipotenusa))

