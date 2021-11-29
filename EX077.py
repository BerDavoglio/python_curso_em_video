palavras = ('pateta', 'chorao', 'desbocado', 'beliscao', 'amor', 'ressentimento', 'todos', 'nenhum', 'protese')
vogais = ('A', 'E', 'I', 'O', 'U')
print('=-'*20)
for c in palavras:
    c = c.upper()
    a = 0
    print(f'As vogais da palavra {c} são:')
    for b in vogais:
        a = c.count(b)
        if a != 0:
            print(f'O número de letras {b} é {a}')
    print('=-'*20)
print('Obrigado.')
