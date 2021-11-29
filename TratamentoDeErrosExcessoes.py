'''
try:
    # Operação
except: # Um try pode ter diversos 'except' diferentes!
    # Erro
# except Exception as erro:
    #Erro; cria a variavel 'erro', onde pode mostrar qual foi o erro encontrado.
else: # Opcional!
    # Deu certo.
finally: # Opcional!
    # Deu certo/Deu Erro.

try:
    a = int(input('Digite um valor para o numerador: '))
    b = int(input('Digite um valor para o denominador: '))
    r = a / b
except Exception as erro:
    print('Não foi possivel realizar a operação...')
    print(f'Erro encontrado: {erro.__class__}')
except ZeroDivisionError:
    print('Não é possivel dividir por zero!')
except KeyboardInterrupt:
    print('Não foi digitado nenhum valor!')
else:
    print(f'O resultado da operação é igual a {r:.1f}.')
finally:
    print('Obrigado!')

'''
