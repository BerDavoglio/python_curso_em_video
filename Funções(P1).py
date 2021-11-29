'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)

#Programa principal:
soma(4, 5)
soma(9, 1)
#É possivel definir qual é o parametro utilizado, podendo inverter a com b.
soma(b=34, a=42) #ou soma(a=34, b=42)


def contador(*num): #Utilizando o parametro *num, criará uma tupla do pacote, não importando o tamanho dele...
    s = 0
    for v in num:
        s += v
    print(f'A soma dos valores {num} é igual a {s}.')

#Programa principal:
contador(1, 4, 5, 2)
contador(3, 8, 6, 42)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

#Programa principal:
valores = [1, 4, 7, 12, 42]
dobra(valores)
print(valores)

'''
