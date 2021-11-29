s = 0
t = 0
for c in range(0, 500, 6):
    s += c
for d in range(0, 500, 3):
    t += d
print('A soma dos termos Impares, multiplos de 3, que estão entre 1 e 500 é igual a {}. '.format(t - s))
print('Obrigado!')
