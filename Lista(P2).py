'''
teste = list()
teste.append('Bernardo')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 27
galera.append(teste[:])
print(galera)

galera = [['João', 32], ['Anna', 14], ['Pedro', 13], ['Julia', 24]]
print(galera)
print(galera[1])
print(galera[3][0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galeras = list()
dados = list()
maior = menor = 0
for c in range(0, 5):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galeras.append(dados[:])
    dados.clear()
for p in galeras:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Tem {maior} pessoas maiores de idade, e {menor} menores de idade.')

'''
