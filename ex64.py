from random import randint
from time import sleep
v = 0

while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}. Total de {total} ')
    print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            v += 1
    elif tipo == 'SAIR':
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente???')
    sleep(1.5)
print(f'Fim do jogo! Voce venceu {v} vezes.')