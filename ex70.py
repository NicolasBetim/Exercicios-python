num = (int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')))

print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu na {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª')
else:
    print('O valor 3 nao foi digitado em nenhuma posiçao')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n,end=' ')