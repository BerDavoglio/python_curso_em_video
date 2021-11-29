def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! DIGITE NOVAMENTE...')
        if ok:
            break
    return valor


n = LeiaInt('Digite um valor: ')
print(f'O número digitado foi {n}.')
