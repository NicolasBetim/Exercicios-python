n = input('Digite seu nome completo:').strip()
nome = n.split()
print('Seu primeiro nome é {}\n'
      'Seu ultimo nome é {}'.format((nome[0]).capitalize(), (nome[len(nome)-1].capitalize())))