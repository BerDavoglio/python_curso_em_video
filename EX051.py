a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for c in range(0, 10):
    print('Termo {} ='.format(c + 1), a + (c * r))
