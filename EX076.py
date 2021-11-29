loja = ('Lapis ', 1.5,
        'Caneta ', 2,
        'Caderno Sulfite ', 5,
        'Kit Lapis de cor ', 10,
        'Material Dourado ', 20,
        'CD ADTR ', 15,
        'Computador ', 550,
        'Fone de ouvido', 350,
        'Teclado', 450,
        'Computador', 1450)
n1 = 0
n2 = 1
print('=-' * 20)
print('{:-^40}'.format(' Tabela de Preços '))
print('=-' * 20)
while True:
    print('{:.<30} R${:>7.2f}'.format(loja[n1], loja[n2]))
    n1 += 2
    n2 += 2
    if n1 == len(loja):
        break
print('=-' * 20)
print('Fim!')
