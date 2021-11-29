import math

cat1 = float(input('Digite um cateto: '))
cat2 = float(input('Digite o outro cateto: '))

hip = math.hypot(cat1, cat2)

print('=-='*25)
print('O triangulo com os catetos {} e {} possui uma hipotenusa de {}.'.format(cat1, cat2, hip))
print('=-='*25)
