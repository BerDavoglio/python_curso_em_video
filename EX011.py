h = float(input('Quantos metros de altura essa parede tem? '))
l = float(input('Quantos metros de largura essa parede tem? '))

a = h * l
t = a / 2

print('A parede selecionada tem {}m² de área, portanto precisará de {} litros de tinta.'.format(a, t))
