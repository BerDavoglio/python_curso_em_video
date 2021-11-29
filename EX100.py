def somapar(lis):
    s = 0
    for c in lis:
        if c % 2 == 0:
            s += c
    print(f'A soma de todos os pares da lista é igual a {s}.')


def sorteio(lis):
    a = choice(lis)
    print(f'O valor selecionado aleatoriamente foi {a}')


from random import randint, choice

lista = [randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5)]
print(f'A lista é composta pelos termos {lista}.')
somapar(lista)
sorteio(lista)
print('Obrigado!')
