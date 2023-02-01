"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta="queijo"
letra_acertada=""
i=0
import os
while True:
   letra_digitada=input('Digite uma letra que você acha que vai tar na palavra: ') 
   i+=1

   if len(letra_digitada)> 1:
    print("Por favor digite apenas uma letra")
    continue

   if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

   palavra_formada=''
   for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada +=letra_secreta
        else:
           palavra_formada+="*"
   print(f'palavra:{palavra_formada}')
   
   if palavra_formada == palavra_secreta:
        os.system("cls")
        print('PARABÉNS, VOCÊ ACERTOU')
        print(f'A palavra é: "{palavra_secreta}"')
        print(f"Você fez {i} tentativas")
        letra_acertada=""
        i=0


        

