sal = float(input('Qual o seu salário R$?'))
if sal > 1250:
   aumento = (sal * 10 / 100) + sal
   print('Seu novo salario é de {:.2f}'.format(aumento))
else:
    aumento = (sal * 15 / 100) + sal
    print('Seu novo salario é de R${:.2f}'.format(aumento))