print('GERADOR DE PA')
print('-='*10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ',end='')
        termo += razao
        cont += 1
    print('Pausa!')
    mais = int(input('Quantos termos voce quer mostrar a mais?'))
print(f'Prograssão finalizada com {total} termos mostrados.')
print('FIM!')