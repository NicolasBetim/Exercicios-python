'''Sem Importação
op = float(input('Valor do Cateto Oposto'))
adj = float(input('Valor do Cateto Adjacente'))
hip = (op ** 2 + adj ** 2) ** (1/2)
print('O valor da hipotenusa é: {:.2f}'.format(hip))
'''

from math import hypot
op = float(input('Valor do Cateto Oposto'))
adj = float(input('Valor do Cateto Adjacente'))
hip = hypot(op, adj)
print('A hipotenusa vai medir {:.2f}'.format(hip))