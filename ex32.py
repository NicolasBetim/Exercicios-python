n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
n3 = int(input('Digite mais um numero:'))
lista = [n1, n2, n3]
print(lista)
if n1 > n3 and n2:
    print('O menor numero é',lista[0])
else:
    print('O menor numero é', lista[2])