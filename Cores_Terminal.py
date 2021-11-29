'''
\033[STYLE;TEXT;BACKmTEXTO
ex:print('\033[1;33;44mOlá, mundo!')
ex2:print('\033[30;47mOlá Mundo!\033[m')

nome = 'Bernardo'
print('Prazer em te conhecer {}{}{}'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'pretobranco':'\033[7;30m',
         'vermelhobranco':'\033[31;40m'}
print('Prazer {}{}{}'.format(cores['vermelhobranco'], nome, cores['limpa']))

'''
