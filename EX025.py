nom = str(input('Digite seu nome completo: ')).strip()

mai = nom.upper()
#Jeito certo de fazer:
print('{:=^30}\n'
      'Seu nome possui Silva? {}.\n'
      '{:=^30}\n'.format('','SILVA' in mai, ''))

#Jeito Não Ortodoxo de fazer:
sil = mai.find('SILVA')
if sil >= 0:
    print('{:=^30}\n'
          'Seu nome possui Silva.\n'
          '{:=^30}\n'.format('', ''))
else:
    print('{:=^30}\n'
          'Seu nome NÃO possui Silva.\n'
          '{:=^30}\n'.format('', ''))
