n = int(input('Digite o valor a ser sacado: '))
c = v = d = u = 0
while True:
    if n // 50 > 0:
        c += (n // 50)
        n -= 50 * (n // 50)
    elif n // 20 > 0:
        v += (n // 20)
        n -= 20 * (n // 20)
    elif n // 10 > 0:
        d += (n // 10)
        n -= 10 * (n // 10)
    elif n // 1 > 0:
        u += (n // 1)
        n -= (n // 1)
    else:
        break
print(f'''O número de cédulas é:
{c} CÉDULAS DE 50 REAIS;
{v} CÉDULAS DE 20 REAIS;
{d} CÉDULAS DE 10 REAIS;
{u} CÉDULAS DE 1 REAL.

OBRIGADO!''')
