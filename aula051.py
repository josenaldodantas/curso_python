'''
Introdução ao desempacotamento + tuples (tuplas)
'''
nomes = ['Maria','Helena', 'Joana', 'Luiz']
nome1, nome2, nome3, nome4 = nomes
nome1, *resto =  ['Maria','Helena', 'Joana', 'Luiz']
print(nome1)

print(resto)
