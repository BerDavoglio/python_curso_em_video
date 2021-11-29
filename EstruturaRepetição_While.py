'''
for c in range(1, 10):
    print(c)
print('Fim!')

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim!')

for c in range(1, 5):
    i = int(input('Digite um valor: '))
print('Fim!')

c = 1
while c != 0:
    c = int(input('Digite um valor: '))
print('Fim!')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor inteiro: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('Fim!')

n = 1
p = 0
i = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0 and n != 0:
        p += 1
    elif n % 2 == 1:
        i += 1
print('Você digitou {} números PARES; {} números IMPARES.'.format(p, i))

'''
