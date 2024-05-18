# Faça uma lista de compras
'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.'''
import os
lista = []

while True:
    print ('Selecione uma opção')
    opcao = input('[i]nserir [a]apagar [l]istar:  ')   
    if opcao == 'i':
        os.system('cls')
        valor = input('Digite o item: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print ('Po favor digite um número int.')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('nada a listar : ')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor escolha [a],[i] ou [l] ')


