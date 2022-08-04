num = int(input('Digite um numero inteiro'))
print('''Escolha uma das bases para conversão
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')

opcao = int(input('Sua Opção:'))
if opcao == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para binario é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para binario é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')