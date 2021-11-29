"""
CURSO PYTHON #09

#Fatiamento:
frase = 'Eu sou inteligente'
    #E u   s o u   i n t  e  l  i  g  e  n  t  e
    #0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
print(frase)
print(frase[9]) #'t'
print(frase[9:13]) #'teli', é excluido o caracter 13.
print(frase[9:18:2]) #'tlgne', é pulado de 2 em 2.
print(frase[:5]) #'Eu so', começa desde o incio e termina um antes do 5.
print(frase[7:]) #'inteligente', começa no caracter 7 e termina no final.
print(frase[9::3]) #'tin', começa no caracter 9, termina no final, e pula de 3 em 3.

#Análise:
frase = 'Eu sou inteligente'
    # E u   s o u   i n t  e  l  i  g  e  n  t  e
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
print(frase)
print(len(frase)) #Numero de caracteres
print(frase.count('e')) #Contar quantos 'e' tem na frase.
print(frase.count('i', 0, 7)) #Contar quantos 'i' tem na frase entre o caracter 0 a 6.
print(frase.find('int')) #Encontrar onde começa o bloco 'int', e quantos tem dentro da frase.
print(frase.find('Android')) #Não existe esse bloco, então o programa resultará -1.
print('sou' in frase) #Se existe 'sou' na frase.

#Transformações:
frase = 'Eu sou inteligente'
    # E u   s o u   i n t  e  l  i  g  e  n  t  e
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
print(frase)
print(frase.replace('inteligente', 'lindo')) #Trocar 'inteligente' por 'lindo'.
print(frase.upper()) #Deixar todas as letras em maiusulas.
print(frase.lower()) #Deixar todas as letras em minusculas.
print(frase.capitalize()) #Apenas o primeiro caracter em maiusculo.
print(frase.title()) #Vai deixar todas as primeiras letras maiusculas.

frase2 = '  Eu sou lindo  '
    #     E u   s o u   l  i  n  d  o
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
print(frase2)
print(frase2.strip()) #Retira os espaços inúteis no inicio e no final da string.
print(frase2.rstrip()) #Retira os espaços inúteis no final da string.
print(frase2.lstrip()) #Retira os espaços inúteis no inicio da string.

#Divisão:
frase = 'Eu sou inteligente'
    # E u   s o u   i n t  e  l  i  g  e  n  t  e
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
print(frase.split()) #Separa cada bloco da string.
d = frase.split()
print(d[1][2]) #Mosta a terceira (2) letra da segunda (1) palavra da lista.

#Junção:
m = frase.split()
print('-'.join(m)) #Junta os blocos em uma string só.

Bizu:
print("""'You better practice your lines'
'You better practice your words'
'I know that real monsters lie'
'Between the light and the shade'
'It doesn''t matter what you say or feel'
'When honest men become deranged'
'They''ll genuflect to a lie'""") #Usar 3 aspas duplas para escrever um texto muito grande.

"""
