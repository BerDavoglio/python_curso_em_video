cs = ('NAVI', 'Astralis', 'G2', 'mousesports', 'fnatic', 'Liquid', 'Evil Geniuses', '100Thieves', 'Vitality', 'FaZe',
      'Furia', 'NiP', 'MAD Lions', 'Complexity', 'OG', 'Gen.G', 'GODSENT', 'Heroic', 'BIG', 'Virtus.pro')
furia = cs.index('Furia') + 1
sortido = sorted(cs)
print('=-'*40)
print(f'Os cinco primeiros times são {cs[0:5]}')
print(f'Os quatro ultimos times são {cs[-4:]}')
print('Os times em ordem de nome ficam: ')
for pos, c in enumerate(sorted(cs)):
    print(f'    {pos + 1} - {c}')
print(f'O time Brasileiro FuriaGG esta na posição {furia} do ranking!')
print('\nOBRIGADO!\n')
print('=-'*40)
