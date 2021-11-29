valores = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    esc = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    if esc in 'N':
        break
    elif esc not in 'S':
        while esc != 'S':
            print('DIGITAÇÃO INVÁLIDA!')
            esc = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('-='*17)
print(f'A lista completa é {valores};\n'
      f'A lista dos pares é {pares};\n'
      f'A lista dos impares é {impares}.')
print('-='*17)
