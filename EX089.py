lnota = list()
dadodenota = list()
dado = list()
m = cont = val = num = 0
while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    m = (nota1 + nota2) / 2
    dado.append(nome)
    dado.append(m)
    lnota.append(nota1)
    lnota.append(nota2)
    dadodenota.append(lnota[:])
    lnota.clear()
    num += 1
    esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc in 'N':
        break
print('-='*20)
print('{:^20}'.format('BOLETIM'))
print('-='*20)
while True:
    print(f'Aluno {cont} - {dado[val]}, média {dado[val + 1]}')
    cont += 1
    val += 2
    if cont == num:
        break
print('-='*20)
while True:
    esco = int(input('Deseja ver as notas de qual aluno? (999 para finalizar) '))
    if esco == 999:
        break
    else:
        print(f'As notas d@ alun@ {esco} são {dadodenota[esco]}...')
print('Programa finalizado com sucesso!')
