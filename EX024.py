city = str(input('Digite o nome da sua cidade: ')).strip()

prim = city.split()[0]
prim1 = prim.upper()
if prim1 == 'SANTO':
    print('{:=^50}\n'
          'A cidade {} começa com a palavra santo =D\n'
          '{:=^50}'.format('', city, ''))
else:
    print('{:=^50}\n'
          'A cidade {} NÃO começa com a palavra santo =D\n'
          '{:=^50}'.format('', city, ''))
