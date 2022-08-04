'''from math import factorial
n = int(input('Digite um numero para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}!')'''

from time import sleep
n = int(input('Digite um numero para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ')
sleep(1)
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

"""from time import sleep
n = int(input('Digite um numero para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando...')
sleep(1)
for c in range (1, n+1):
    f *= c
    c -= 1
print(f'{n}! = {f}')"""