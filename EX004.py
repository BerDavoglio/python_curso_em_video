a = input('Digite algo: ')

type = type(a)
espaços = a.isspace()
num = a.isnumeric()
alf = a.isalpha()
alnum  = a.isalnum()
mai = a.isupper()
min = a.islower()
cap = a.istitle()

print('A coisa que você digitou é do tipo {}; \n' 
      'É feita somente de espaços? {}; \n'
      'É um número? {}; \n'
      'É Alfabético? {}; \n'
      'É Alfanumérico? {}; \n'
      'Está em maiúsculo? {}; \n'
      'Está em minusculo? {}; \n'
      'Está capitalizada? {}.'. format(type, espaços, num, alf, alnum, mai, min, cap))
