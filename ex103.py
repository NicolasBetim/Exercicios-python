def ficha(jog='<desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol}(s) no campeonato.')


# Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strp() == '':
    ficha(gol=g)
else:
    ficha(n, g)
