salario = float(input('Qual o salario do Funcionario R$'))
porcentagem = float(input('Qual a porcentagem do aumento R$'))
reajuste = salario * porcentagem / 100
newSalario = salario + reajuste
print('O reajuste foi de R${:.2f}\n'
      'E seu novo salário é de R${:.2f}'
      .format(reajuste, newSalario))