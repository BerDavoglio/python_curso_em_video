from random import randint
palpite = list()
totpalpite = list()
c = 0
quantos = int(input('Digite quantos palpites você deseja: '))
while c < quantos:
    cont = 0
    while True:
        n = randint(0, 60)
        if n not in palpite:
            palpite.append(n)
            cont += 1
        if cont == 6:
            break
    palpite.sort()
    totpalpite.append(palpite[:])
    palpite.clear()
    c += 1
print(f'Os palpites foram:')
for i, c in enumerate(totpalpite):
    print(f'{i + 1}º palpite = {c}...')
print('Fim!')
