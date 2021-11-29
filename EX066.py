n = s = c = 0
while True:
    n = int(input('Digite um valor [999 para finalizar]: '))
    if n == 999:
        break
    s += n
    c += 1
p = '=-'*20
print(p)
print(f'A soma dos {c} números é igual a {s}.\n'
      f'OBRIGADO!')
print(p)