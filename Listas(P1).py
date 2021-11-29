'''
Listas estão entre COUXETES []
Listas são MUTÁVEIS

lista = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lista[2] = 'Sorvete'
lista.append('Biscoito') #É o comando que faz a lista receber um novo valor.
lista.insert(0, 'Macarrão') #É o comando que faz a lista receber um novo valor em um lugar específico.
lista.pop(3) #Deleta um valor específico, igual o comando 'del lista[3]'; se o pop n tiver valor, ele removerá o ultimo.
lista.remove('Suco') #Caso tenha elementos repetidos, ele apenas remove o primeiro termo.
#TODA REMOÇÃO/ATRIBUIÇÃO DE VALORES AUTOMATICAMENTE ARRUMA A NUMERAÇÃO DA LISTA.
print(lista)

valores = list(range(4, 11))
valores = [8, 4, 5, 3, 6, 21, 42]
valores.sort() #Ordena os valores colocados em ordem crescente.
valores.sort(reverse=True) #Ordena os valores colocados em ordem decrescente.
len(valores) #Número de termos da Lista
print(valores, len(valores))

valores = list() #Poderia ser substituida pelo comando 'valores = []'
valores.append(5)
valores.append(9)
valores.append(42)
valores.append(3)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c+1}, foi encontrado o valor {v}.')
print('Acabou!')

a = [2, 4, 7, 9]
b = a #Quando é igualada duas listas, o python cria uma ligação entre elas, fazendo ser impossivel mudar uma
      # sem mudar a outra diretamente.
b[2] = 13

b = a[:] #Fazendo B copiar todos os itens de A, faz com que ele seja uma cópia, e n forme a ligação.
b[2] = 13
print(f'A lista A: {a}')
print(f'A lista B: {b}')

'''
