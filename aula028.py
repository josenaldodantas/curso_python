"""""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade:')
nome_iv = (nome[::-1])

print ( f' Seu nome é : {nome}' )
print ( f' Sua idade é : {idade}')
print ( f' Seu nome invertido é : {nome_iv}')

if nome and idade:
    ...
else:
    print( "Desculpe, você deixou campos vazios.")

    if ' ' in nome:

        print('Seu nome contem espaços')
    else:
        print('Seu nome não contém espaços')

    print(f' Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é ')    
    print(f'A Primeira letra do seu nome é {nome[0]}')
    print(f'A Ultima letra do seu nome é {nome[-1]}')











