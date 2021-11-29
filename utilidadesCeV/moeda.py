def aumentar(num, porc, moe):
    if moe == 'F':
        return num + (num * (porc / 100))
    else:
        n = f'R${num + (num * (porc / 100)):.2f}'
        return n.replace('.', ',')


def diminuir(num, porc, moe):
    if moe == 'F':
        return num * (1 - (porc / 100))
    else:
        n = f'R${num * (1 - (porc / 100)):.2f}'
        return n.replace('.', ',')


def dobro(num, moe):
    if moe == 'F':
        return num * 2
    else:
        n = f'R${num * 2:.2f}'
        return n.replace('.', ',')


def metade(num, moe):
    if moe == 'F':
        return num / 2
    else:
        n = f'R${num / 2:.2f}'
        return n.replace('.', ',')


def moeda(num):
    n = f'R${num:.2f}'
    return n.replace('.', ',')


def resumo(num):
    porc = 15
    print('=-' * 24)
    print(f'O aumento de {porc}% no valor é igual a {aumentar(num, porc, moe="T")}')
    print(f'A redução de {porc}% no valor é igual a {diminuir(num, porc, moe="T")}')
    print(f'O dobro do valor é igual a {dobro(num, moe="T")}')
    print(f'A metade do valor é igual a {metade(num, moe="T")}')
    print('=-' * 24)
