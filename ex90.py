dados = dict()
dados['Nome'] = str(input('Nome do Aluno: '))
dados['Média'] = float(input('Média do aluno: '))
if dados['Média'] >= 7:
    dados['situação'] = 'APROVADO!'
elif dados['Média'] <= 6.9 and dados['Média'] > 5:
    dados['situação'] = 'RECUPERAÇÂO!'
else:
    dados['situação'] = 'REPROVADO!'
print('__' * 30)
for k, v in dados.items():
    print(f'{k} é igual a {v}')