palavra_secreta = 'ferramenta'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
         print('Digite apenas uma letra. ')
         continue
  
    if letra_digitada in palavra_secreta:
      letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
    else:
          palavra_formada +=  '*'        

    print('Palavra Formada:',palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Voce Ganhou !! Parabéns!') 
        print('A Palavra Secreta ERA:', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0


    
    
    
