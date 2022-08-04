from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior/Menor
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>> Qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f' A soma entre {n1} e {n2} é {soma}.')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'O produto entre {n1} e {n2} é {multiplicacao}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'Entre {n1} e {n2} o maior valor é {maior}')
        elif n1 < n2:
            maior = n2
            print(f'Entre {n1} e {n2} o maior valor é {maior}')
        else:
            print(f'{n1} e {n2} são iguais!')

    elif opcao == 4:
        print('Digite os números novamente!')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo valor:'))

    elif opcao == 5:
        print ('Finalizando...')
        sleep(1)
    else:
        print('Digite uma opção valida!\n')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!!!')