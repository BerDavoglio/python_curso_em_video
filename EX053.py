f = str(input('Digite uma frase (sem acento ou simbolos): '))
alt = f.upper()

mu = ''.join(alt.split())[::-1]

print('A fase digitada foi "{}" '.format(f))
if ''.join(alt.split()) == mu:
    print('Essa frase É UM PALINDROMO.')
else:
    print('Essa frase NÃO É UM PALINDROMO.')
