import math

anggraus = float(input('Digite o valor do Ângulo desejado (em graus): '))

angrad = math.radians(anggraus)
sin = math.sin(angrad)
cos = math.cos(angrad)
tg = math.tan(angrad)

print('=-='*10)
print('O angulo escolhido foi {}.\n'
      'O seno dele vale {:.2f}\n'
      'O cosseno dele vale {:.2f}\n'
      'A tangente dele vale {:.2f}.'.format(anggraus, sin, cos, tg))
print('=-='*10)