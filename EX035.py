from math import sqrt

l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

if sqrt((l1 - l2) ** 2) < l3 < l1 + l2:
    print('Os lados {}, {}, {} FORMARÃO um triangulo!'.format(l1, l2, l3))
else:
    print('Os lados {}, {}, {} NÃO FORMARÃO um triangulo!'.format(l1, l2, l3))
