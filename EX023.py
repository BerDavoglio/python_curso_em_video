num = int(input('Digite um valor inteiro entre 0 e 9999: '))

un = num % 10
de = ((num % 100) - un) // 10
ce = ((num % 1000) - de - un) // 100
mi = ((num % 10000) - ce - de - un) // 1000

print('O valor digitado foi: {};\n'
      '{:=^30}\n'
      'A Unidade dele vale: {};\n'
      'A Dezena dele vale: {};\n'
      'A Centena dele vale: {};\n'
      'O Milhar dele vale: {};\n'
      '{:=^30}\n'
      'Obrigado.'.format(num, '', un, de, ce, mi, ''))
