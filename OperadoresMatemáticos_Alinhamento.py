'''
+ = Adição
- = Subtração
* = Multiplicação
/ = Divisão
** = Potência
// = Divisão inteira
% = Resto da divisão
== = Igualdade
!= = Desigualdade

Ordem de Precedência:
    1 - ()
    2 - **
    3 - * / // %
    4 - + -

n1 ** n2 == pow(n1,n2)

'='*5 == '====='

Alinhamento:
    nome = input('Qual é o seu nome? ')
    print('Prazer em te conhecer {:10}!'.format(nome))
        #'Prazer em te conhecer Nome          !'
    print('Prazer em te conhecer {:>10}!'.format(nome))
        #'Prazer em te conhecer           Nome!'
    print('Prazer em te conhecer {:^10}!'.format(nome))
        #'Prazer em te conhecer      Nome     !'
    print('Prazer em te conhecer {:=^10}!'.format(nome))
        #'Prazer em te conhecer =====Nome=====!'


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

som = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
pot = n1 ** n2
dii = n1 // n2
dir = n1 % n2

print('Os números escolhidos foram {} e {};\n'
      'A soma entre eles resultou {};\n'
      'A subtração de {} menos {} resultou {};\n'
      'A multiplicação entre eles resultou {};\n'
      'A divisão de {} sobre {} resultou {:.3f};\n'     #{:.3f} significa a redução das casas decimais em 3 casas flutuantes.
      '{} elevado à {} é igual a {};\n'
      'O valor inteiro da divisão é {};\n'
      'O resto da divisão é {}.'.format(n1, n2, som, n1, n2, sub, mul, n1, n2, div, n1, n2, pot, dii, dir))

'''

#Des7:

