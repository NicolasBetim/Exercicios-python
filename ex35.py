casa = float(input('Qual o valor da casa R$?'))
sal = float(input('Qual o seu salario R$?'))
anos = int(input('Em quantos anos vai pagar?'))

prest = casa / (anos * 12)
sal30 = (sal * 30 / 100)

if prest > sal30:
    print('Desculpe! Prestação excedeu o seu limite')

else:
    print('Parabéns!! Seu financiamento foi liberado')