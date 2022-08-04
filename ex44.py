soma = 0
cont = 0
for c in range(1,501,):
    if c % 3 == 0:
        cont = cont + 1
        soma =+ c
print(f'A soma de {cont} todos os numeros solicitados é {soma}')