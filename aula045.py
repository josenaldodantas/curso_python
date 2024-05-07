'''
Iteravel -> str, range , etc  (__iter___)
iterador -> quem sabe entregar um valor por vez
next  -> me entregue o proximo valor
iter -> me entregue seu iterador

'''
# For + range
# range > range(start, stop, step)
'''
texto = iter('Paralelepipido')

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(next(texto))
print(next(texto))

'''
'''
texto = " portugal"
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break    
'''
texto = 'Portugal'
for letra in texto:
    print(letra)
