'''
while True:
    if ... :
    elif ... :
    elif ... :
        break #Comando para INTERROMPER o WHILE.
    elif ... :
    else:
print('Fim!')

n = 1
while True: #Ele vai executar a estrutura WHILE para sempre!
    print(n, ' ', end='')
    n += 1
print('\nFim!')

n = s = 0
while n != 999:
    n = int(input('Digite um valor: '))
    s += n
s -= 999
print('A soma vale {}.'.format(s))

n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
print('A soma vale {}.'.format(s))

n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')
#BIZU: se colocar f antes das '', pode se colocar a variável dentro das chaves, ao invés do .format()...

'''