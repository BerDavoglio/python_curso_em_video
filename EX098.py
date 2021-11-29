from time import sleep

def contador(i, f, p):
    print('-='*30)
    for c in range(i, f + 1, p):
        print(f'{c} -> ', end='', flush=True)
        sleep(0.5)
    print('Fim!')


contador(10, 0, -2)
contador(1, 10, 1)
inicio = int(input('Digite onde parte a contagem: '))
fim = int(input('Digite até onde deseja a contagem: '))
passo = int(input('Digite o passo da contagem: '))
if inicio > fim:
    fim -= 2
    if passo > 0:
        passo = abs(passo) * -1
elif passo == 0:
    passo = 1
contador(inicio, fim, passo)
