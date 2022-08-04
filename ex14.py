km = float(input('Quantos KM o carro rodou?'))
dias = int(input('Por quantos dias ele foi alugado?'))
precoKm = km * 0.15
precoDia = dias * 60
total = precoDia + precoKm
print('O valor total por km rodado é de R${:.2f}\n'
      'O valor total do aluguel por dia é de R${}\n'
      'O valor total da conta é de R${:.2f}.'
      .format(precoKm, precoDia, total))