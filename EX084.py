lista = list()
dado = list()
pesos = list()
nomemax = list()
nomemin = list()
cont = indicemax = indicemin = 0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite o peso: ')))
    lista.append(dado[:])
    dado.clear()
    cont += 1
    esc = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if esc in 'N':
        break
for c in range(0, cont):
    pesos.append(lista[c][1])
for i, d in enumerate(lista):
    if max(pesos) in lista[i]:
        nomemax.append(lista[i][0])
        indicemax = i
    if min(pesos) in lista[i]:
        nomemin.append(lista[i][0])
        indicemin = i

print('-='*24)
print(f'Foram cadastradas {cont} pessoas no total;\n'
      f'O maior peso foi {max(pesos)}, e {nomemax} possuem ele;\n'
      f'O menor peso foi {min(pesos)}, e {nomemin} possuem ele.')
print('Obrigado!')
print('-='*24)
