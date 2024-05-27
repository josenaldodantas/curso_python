"""
Ecercícios com funções
Crie uma função que multiplica todos os argumentos não nomeados recebidos
retorne o total para uma variavel e mostre o valor da variavel
"""
def multiplicacao (*args):
    total = 1
    for numero in args:
        total *= numero 
    return total   
 
multiplicar = multiplicacao(1,2,3,4,5)

print(multiplicar)



# Crie uma função e diga se um numero é par ou impar
# retorne se o número é par ou ímpar

def par_imp (numero):
   multiplo = numero % 2 == 0

    if multiplo:
       

    return numero % 2 ==0
    
print(par_imp(2))
print(par_imp(5))
print(par_imp(7))
print(par_imp(10))
