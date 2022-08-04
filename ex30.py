dist = int(input('Qual a distancia da viagem?'))
if dist <= 200:
    preço = dist * 0.50
    print('O valor da sua passagem é de {:.2f}'.format(preço))
else:
    preço = dist * 0.45
    print('O valor da sua passagem é de {:.2f}'.format(preço))