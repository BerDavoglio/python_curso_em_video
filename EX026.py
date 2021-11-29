fraz = str(input('Digite uma frase: ')).strip()

num = fraz.upper().count('A')
ond = fraz.upper().find('A') + 1
enc = len(fraz) - fraz.upper()[::-1].find('A')

print('A frase digitada foi: \n'
      '{}\n'
      'Ela possui {} letras A;\n'
      'O primeiro A esta na posição {};\n'
      'E o ultimo A esta na posição {};\n'
      'Obrigado.'.format(fraz, num, ond, enc))
