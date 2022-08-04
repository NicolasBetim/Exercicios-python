dinheiro  =  float ( input ( 'Quantos reais voce tem R$?' ))
print ( 'Com R${:.2f} voce consegue comprar: \n '
      '{:.2f} Dolares! \n '
      '{:.2f} Euros! \n '
      '{:.2f} Pesos!' . formato ( dinheiro , ( dinheiro  /  5,33 ), ( dinheiro / 6,42 ), ( dinheiro / 0,60 )))