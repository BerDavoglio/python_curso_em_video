nom = str(input('Digite seu nome completo: ')).strip()

prim = nom.split()[0].title()
inv = nom[::-1].split()[0][::-1].title()

print('O nome digitado foi: {};\n'
      'O primeiro nome é {};\n'
      'O ultimo nome é {};\n'
      'Obrigado.'.format(nom, prim, inv))
