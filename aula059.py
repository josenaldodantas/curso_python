# desempacotamento em chamadas
# de métodos e funções
string = "ABCDE"
lista = ['Maria', 'Helena', 1, 2, 3, 'Maria Eduarda']
tupla = 'Python', 'é', 'Legal'

a, b, *_, ap, c= lista
print(a, ap)

for nome in lista:
    print(nome, end=' ')
print(*lista)
print(*string)
print(*tupla)

