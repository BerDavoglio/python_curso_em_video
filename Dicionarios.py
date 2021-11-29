'''
Chaves são representadas por {}

dados = {'nome': 'Bernardo', 'idade': 19}
dados['sexo'] = 'M' #Adicionar uma nova variavel dentro do dicionario
del dados['idade'] #Remover um valor dentro do dicionario


filmes = {
    'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'
}
print(filmes.values()) #Mostrara os valores dentro do dicionario
print(filmes.keys()) #Mostra os compartimentos do dicionario
print(filmes.items()) #Mostra tanto o values() quanto o keys()

for k, v in filmes.items():
    print(f'O {k} é {v}')
locadora = list()
locadora.append(filmes)
filmes = {
    'titulo': 'Vingadores', 'ano': 2012, 'diretor': 'Joss Whedon'
}
for k, v in filmes.items():
    print(f'O {k} é {v}')
locadora.append(filmes)
print(locadora)
print(locadora[1]['diretor'])


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Digite o UF: '))
    estado['sigla'] = str(input('Digite a SIGLA: '))
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} possui {v} como valor...')

'''
