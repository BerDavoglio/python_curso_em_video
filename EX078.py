lista = list()
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
maximo = max(lista)
minimo = min(lista)
print(f'A lista digitada foi {lista};\n')
print(f'O máximo valor foi {maximo} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maximo:
        print(f'{i}... ', end='')
print()
print(f'O mínimo valor foi {minimo} nas posições ', end='')
for i, v in enumerate(lista):
    if v == minimo:
        print(f'{i}... ', end='')
print()
print('Obrigado.')
