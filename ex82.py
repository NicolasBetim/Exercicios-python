valores = []
valorespares = []
valoresimpares = []
while True:
    nums = int(input('Digite um valor: '))
    valores.append(nums)
    if (nums % 2) == 0:
        valorespares.append(nums)
    else:
        valoresimpares.append(nums)
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Lista de todos os valores: {valores}')
print(f'Lista dos valores pares: {valorespares}')
print(f'Lista dos valores impares: {valoresimpares}')