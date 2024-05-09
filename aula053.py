
#enumerate - enumera iteráveis (índices)
 

lista = ['Maria', 'Helena', 'Kaio']
lista.append('Rick')

lista_enumerada = enumerate(lista)
# lista_enumerada = list(enumerate(lista)) converter para lista

#print(lista_enumerada)
#print(next(lista_enumerada))

#for item in lista_enumerada:
#   print(item)

for indice, nome in enumerate(lista):
    print(indice, nome)
    


