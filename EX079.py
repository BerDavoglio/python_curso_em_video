lista = list()
while True:
    val = int(input('Digite um valor: '))
    if val not in lista:
        lista.append(val)
        print(f'Valor {val} adicionado')
    else:
        print('O valor ja foi adicionado anteriormente...')
    esc = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if esc in 'N':
        break
lista.sort()
print(f'Os valores digitados foram {lista}')
