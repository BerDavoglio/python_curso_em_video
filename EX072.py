numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Qual valor você deseja solicitar? '))
while n > 20 or n < 0:
    n = int(input('Valor inválido, digite outro valor: '))
mostrar = numeros[n]
print(f'\nO número que você escolheu foi o {mostrar}.')
print('\nObrigado!')
