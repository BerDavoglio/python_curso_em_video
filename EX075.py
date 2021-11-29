s = 0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite outro valor: '))
n4 = int(input('Digite outro valor: '))
numeros = (n1, n2, n3, n4)
v9 = numeros.count(9)
if 3 in numeros:
    v3 = f'O valor 3 aparece na posição {numeros.index(3) + 1}'
else:
    v3 = 'Não foi digitado nenhum valor igual a 3'
for c in numeros:
    if c % 2 == 0:
        s += 1
print('')
print(f'O valor 9 aparece {v9} vezes;\n'
      f'{v3};\n'
      f'Foram digitados {s} números PARES.')
print('Obrigado!')
