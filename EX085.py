cont = contpares = contimpares = 0
num = list()
while cont != 7:
    s = int(input('Digite um valor: '))
    if s % 2 == 0:
        num.insert(0, s)
        contpares += 1
    else:
        num.append(s)
    cont += 1
impares = num[contpares:]
pares = num[:contpares]
impares.sort()
pares.sort()
num.sort()
print('')
print(f'Os valores digitados foram {num};\n'
      f'Os pares foram {pares} e os impares foram {impares}.')
print('Obrigado!')
