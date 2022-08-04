reta1 = float(input('Digite o valor da reta 1'))
reta2 = float(input('Digite o valor da reta 2'))
reta3 = float(input('Digite o valor da reta 3'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima NAO podem formar um triangulo')