# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizaveis - indices e fatiamento
# Métodos uteis: append, insert, pop, del, clear, extend, +
# Create, read update delete =del
#    +01234
#    -54321

string = 'ABCDE'


#        0     1       2       3    4
#       -5    -4      -3      -2   -1   
#lista =[123, True, "garrafa", 6.9, []]

#lista[-3] = 'Maria'
#print(lista)
#print(lista[3], type(lista[3]))

lista = [10,20,30,40]
lista[2] = 300
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
#del lista[2]
ultimo_valor = lista.pop(3)
lista.insert(0, 5)
print(lista, 'Removido', ultimo_valor)

# + concatena listas 
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
#lista_a.extend(lista_b)
print(lista_c)
print(lista_d)


#proxima aula 84