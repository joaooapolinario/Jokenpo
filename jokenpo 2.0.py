import random
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = random.randint(0, 2)


começar = str(input('QUER INICIAR?[S/N] ')).upper()
r = começar
if começar == 'n':  
    input('Tecle ENTER para sair')
        
while r == 'S':
    print('''---SUAS OPÇÕES---
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    jogador = int(input('Qual é sua jogada?? '))
    
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!!!')

    print('-=' * 11)
    print('computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)
    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('VOCÊ VENCEU!')
        elif jogador == 2:
            print('VOCÊ PERDEU!')
        else:
            print('JOGADA INVALIDA')
            
    elif computador == 1:
        if jogador == 0:
            print('VOCÊ PERDEU!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('VOCÊ VENCEU!')
        else:
            print('JOGADA INVALIDA')

    elif computador == 2:
        if jogador == 0:
            print('VOCÊ VENCEU!')
        elif jogador == 1:
            print('VOCÊ PERDEU!')
        elif jogador == 2:
            print('EMPATE!')
        else:
            print('JOGADA INVALIDA')
            
    r = str(input('QUER CONTINUAR??[N/S] ')).upper()

print('Até mais!!!')
            
input('Tecle ENTER para sair!')#serve para que o cmd nao feche automaticamente.

