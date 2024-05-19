"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
# def Print(a, b, c):

#     print('várias1')
#     print('várias2')
#     print('várias3')
#     print('várias4')



# def imprimir(a, b, c):

#     print(a, b, c)
#     print('várias2')
#     print('várias3')
#     print('várias4')
# imprimir(10, 20, 30)
# imprimir(5, 6, 7)

def saudacao(nome='Anonimo'):
    print(f'Olá {nome} Seja Bem Vindo!')

saudacao('Josenaldo')
saudacao('Jéssica')
saudacao()