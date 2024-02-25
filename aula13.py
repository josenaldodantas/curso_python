nome = "Antonio"
altura = 1.76
peso = 82
imc = peso / (altura * altura)  # IMC = peso / (altura x altura)

# Introdução a f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} Kilos e seu IMC é:'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

print(nome, 'tem', altura, 'de altura',)
print('pesa', peso, 'kilos e seu IMC é:', imc)

