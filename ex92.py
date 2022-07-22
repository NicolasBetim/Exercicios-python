from datetime import datetime
trabalhador = dict()
while True:
    trabalhador['Nome'] = str(input('Nome: '))
    nasc= int(input('Ano de Nascimento: '))
    trabalhador['idade'] = datetime.now().year - nasc
    trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
    if trabalhador['CTPS'] == 0:
        break
    else:
        trabalhador['Contratação'] = int(input('Ano de Contratação: '))
        trabalhador['Salário'] = float(input('Salário: R$'))
        trabalhador['aposentadoria'] = 65 - trabalhador['idade']
        break
print('-='*30)
for k, v in trabalhador.items():
    print(f'{k} tem o valor de {v}')