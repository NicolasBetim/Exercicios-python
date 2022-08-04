times = ('Athletico Paranaense','Atlético Goianiense', 'Atlético Mineiro', 'Bahia', 'Botafogo', 'Ceará', 'Corinthians',
       'Coritiba', 'Flamengo', 'Fluminense', 'Fortaleza	', 'Goiás', 'Gremio', 'Internacional', 'Palmeiras',
       'RB Bragantino', 'Santos', 'Sao Paulo', 'Vasco')

print('-='*20)
print(f'Lista de times do brasileirao:{times}')
print('-='*20)
print(f'Os cinco primeiros colocados são:{times[0:5]}')
print('-='*20)
print(f'Os quatro ultimos sao:{times[-4:]}')
print('-='*20)
print(f'O Corinthians esta na {times.index("Corinthians")+1} posição')
print('-='*20)