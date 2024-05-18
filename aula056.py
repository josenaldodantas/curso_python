frase = 'Olha só que, coisa interessante'
lista_frase_orig = frase.split(',')

lista_frase_corrigidas =[]

for i, frase in enumerate(lista_frase_orig):
    lista_frase_corrigidas.append(lista_frase_orig[i].strip())



print(lista_frase_corrigidas)
print(lista_frase_orig)
frases_unidas = ', '.join(lista_frase_corrigidas)
print(frases_unidas)
