def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show==True:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, True))
print(fatorial(2))
print(fatorial(7, True))
