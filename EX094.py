dados = {}
mulheres = []
maiores = []
pessoas = []
s = idade = m = 0
while True:
    dados['Nome'] = str(input('Digite o NOME: '))
    dados['Sexo'] = str(input('Digite o SEXO: ')).upper().strip()[0]
    dados['Idade'] = int(input('Digite a IDADE: '))
    pessoas.append(dados.copy())
    if dados['Sexo'] in 'F':
        mulheres.append(dados['Nome'])
        m += 1
    dados.clear()
    s += 1
    esc = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if esc in 'N':
        break
print('=-'*30)
#Total de pessoas:
print(f'O total de pessoas cadastradas foram: {s} pessoas!')
#Média das idades:
for c in range(0, s):
    idade += pessoas[c]['Idade']
media = idade / s
print(f'A média da idade das pessoas é: {media} anos!')
#Mulheres cadastradas:
print(f'As mulheres cadastradas foram a ', end='')
for c in mulheres:
    print(c, end='; ')
print('')
#Pessoas mais velhas doque a média:
for d in range(0, s):
    if pessoas[d]['Idade'] > media:
        maiores.append(pessoas[d]['Nome'])
print(f'As pessoas mais velhas que a média são {maiores}.')
print('=-'*30)
print('Obrigado.')
