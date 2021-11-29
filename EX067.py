while True:
    n = int(input('Digite o valor desejado (Para finalizar, digite um valor negativo): '))
    if n < 0:
        break
    p = '=-'*6
    print(p)
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
    print(p)
print('\nFim!')