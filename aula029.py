"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input('Digite um número para dobrar ')

try:
    numero_float = float(numero)
    print('Float:', numero_float)
    print(f'O dobro de {numero} é {numero_float *2:.0f}')
except:
    print('Isso não é um número')
    





    

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')