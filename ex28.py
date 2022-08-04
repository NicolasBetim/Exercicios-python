vel = int(input('Qual a velocidade do carro?'))

if vel <= 80:
    print('Siga!')
else:
    multa = (vel - 80) * 7
    print('Você foi multado. O valor da sua multa é de R${:.2f}'.format(multa))