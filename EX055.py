maior = 0
menor = 0
for p in range(0, 5):
    pn = float(input('Digite as Massas: '))
    if p == 0:
        maior = pn
        menor = pn
    else:
        if pn > maior:
            maior = pn
        if pn < menor:
            menor = pn
print('A maior massa digitada foi {} Kg;\n'
      'A menor massa digitada foi {} Kg.'.format(maior, menor))
