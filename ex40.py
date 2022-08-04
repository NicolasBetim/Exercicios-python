from datetime import date
atual = date.today().year
idade = int(input('Digite seu ano de nascimento'))
categoria = atual - idade
if categoria <= 9:
    print('Sua categoria é MIRIM')
elif categoria > 9 and categoria <= 14:
    print('Sua categoria é INFANTIL')
elif categoria > 14 and categoria <= 19:
    print('Sua categoria é JUNIOR')
else:
    print('Voce ja ta veio!')