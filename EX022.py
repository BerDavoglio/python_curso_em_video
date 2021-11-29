nom = str(input('Digite seu nome completo: ')).strip()

mai = nom.upper()
min = nom.lower()
num = len(''.join(nom.split()))
prim = len(nom.split()[0])

print('O nome digitado foi: {};\n'
      'Esse nome com todas as letras maiúsculas fica: {};\n'
      'Esse nome com todas as letras minúsculas fica: {};\n'
      'O número de letras é igual a {}\n'
      'E o número de letras do primeiro nome é igual a {}.\n'
      'É um prazer conhecer você...'.format(nom, mai, min, num, prim))
