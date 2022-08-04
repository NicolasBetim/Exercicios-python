from math import radians, sin, cos, tan
angle = float(input('Digite o angulo que deseja:'))
seno = sin(radians(angle))
cosseno = cos(radians(angle))
tangente = tan(radians(angle))
print('o angulo de {} tem\n'
      'O seno de {:.2f}\n'
      'O cosseno de {:.2f}\n'
      'A tangente de {:.2f}'
      .format(angle,seno,cosseno,tangente))