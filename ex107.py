import Moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é R${Moeda.metade(p)}')
print(f'O dobro de {p} é R${Moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${Moeda.aumentar(p, 10)}')
print(f'Diminuindo 10%, temos R${Moeda.diminuir(p, 10)}')
