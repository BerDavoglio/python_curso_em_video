def escreva(text):
    print('=' * t)
    print(f'  {text}  ')
    print('=' * t)


texto = str(input('Digite a frase desejada: '))
t = len(texto) + 4
escreva(texto)
