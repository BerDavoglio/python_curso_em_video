from time import sleep

n = int(input('Digite o valor que deseja converter: '))
print('''Escolha a base desejada: 
[1] Binário;
[2] Octal;
[3] Hexadecimal.''')
esc = int(input('Escolha: '))

print('{}\n'
      '\033[1;30mPROCESSANDO... AGUARDE!\033[m\n'
      '{}\n'.format('=-'*12, '=-'*12))
sleep(2)

print('Convertendo o valor {}, fica:'.format(n))
if esc == 1:
    print('{} em Binário.\n'.format(bin(n)[2:]))
elif esc == 2:
    print('{} em Octal.\n'.format(oct(n)[2:]))
elif esc == 3:
    print('{} em Hexadecimal.\n'.format(hex(n)[2:]))
else:
    print('\033[1;30;41mESCOLHA INVÁLIDA\033[m\n')

sleep(1)
print('{}\n'
      '\033[1;30mOBRIGADO!\033[m\n'
      '{}'.format('=-'*5, '=-'*5))
