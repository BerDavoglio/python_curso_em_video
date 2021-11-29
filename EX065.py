n = 0
m = 0
a = 0
s = 'S'
maior = 0
menor = float('inf')

while s in ('Ss'):
    n = int(input('Digite um valor: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    m += n
    a += 1
    s = str(input('Deseja continuar?[ S / N ] '))

media = m / a

print('''A média dos valores é igual a {};
O maior valor digitado foi {};
O menor valor digitado foi {};

Obrigado!'''.format(media, maior, menor))
