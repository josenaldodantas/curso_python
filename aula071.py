'''
args - Argumentos não nomeados 
*_*args (empacotamento e desempacotamento)
'''
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
    # return x + y
 
def soma (*args):
    total = 0
    for numero in args:
        # total = total + numero 
        total += numero
        print(numero, total)
    return total    
 
soma(1, 2, 3, 4, 5, 6)
print(sum((1,2,3,4,5,6)))
\
numeros = 1,2,3,4,5,10,20
print(numeros)
outra_soma= soma(*numeros)
print(outra_soma)
