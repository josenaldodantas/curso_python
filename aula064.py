"""
Gerador de CPF
"""
import re
import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

contador_regressivo_1 = 10

resultador_digito1 = 0
for digito_1 in nove_digitos:
    resultador_digito1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultador_digito1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultador_digito2 = 0
for digito in dez_digitos:
    resultador_digito2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultador_digito2 *10) %11

digito_2 = digito_2 if digito_2 <= 9 else 0
novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'
print (f' O CPF gerado é : {novo_cpf}')



