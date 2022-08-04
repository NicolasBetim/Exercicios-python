from random import choice
lista = [0, 1, 2, 3, 4, 5]
escolhido = choice(lista)
n = int(input('Digite um numero de 0 a 5!'))
if n == escolhido:
    print('Você acertou, parabéns!')
    print('Seu número {}\n'
          'Numero escolhido pelo PC {}'.format (n, escolhido))
else:
    print('Você errou! Tente novamente!')
    print('Seu número {}\n'
          'Numero escolhido pelo PC {}'.format(n, escolhido))