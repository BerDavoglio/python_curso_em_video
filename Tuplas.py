'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1]) #Mostra o 2 termo.
print(lanche[-1]) #Mostra o 1 termo da direita para a esquerda.
print(lanche[1:3]) #Mostra o 2 e o 3 termo, desconsiderando o 4.
print(lanche[1:]) #Mostra do 2 termo até o final.
print(lanche[:3]) #Mostra do início até o 3 termo, desconsiderando o 4 termo.
print(lanche[-2:]) #Mostra do 2 termo da Dir p/ Esq até o final.
print(lanche[:-1]) #Mostra do início até o 1 termo da Dir p/ Esq.
print(len(lanche)) #len() mostra quantos termos tem dentro da tupla.
print(sorted(lanche)) #Colocou em ordem os termos!

#Tuplas são IMUTÁVEIS!!!

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Estava muuuito bom!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Estava muuuito bom!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Estava muuuito bom!')

a = (2, 5, 4)
b = (8, 5, 1, 2)
c = a + b #A soma literal das Tuplas.
print(a)
print(b)
print(c)
print(c.count(5)) #Quantas vezes aparece o termo 5.
print(c.index(8)) #Em qual posição da Tupla esta o termo 8.

pessoa = ('Bernardo', 18, 'M', 69)
del(pessoa)
print(pessoa)

'''
