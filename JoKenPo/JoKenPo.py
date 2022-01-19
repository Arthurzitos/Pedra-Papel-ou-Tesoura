from random import randint
from time import sleep

# U+1F44A = Emoji Pedra
# U+270B = Emoji Papel
# U+270C = Emoji Tesoura
# U+1F91D = Emoji Empate
# U+2716 = Emoji Erro

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('O que você escolhe? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE! \U0001F91D')
    elif jogador == 1:
        print('JOGADOR VENCE! \U0000270B')
    elif jogador == 2:
        print('COMPUTADOR VENCE! \U0001F44A ')
    else:
        print('JOGADA INVÁLIDA! \U00002716' )

elif computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE! \U0000270B')
    elif jogador == 1:
        print('EMPATE! \U0001F91D')
    elif jogador == 2:
        print('JOGADOR VENCE! \U0000270B')
    else:
        print('JOGADA INVÁLIDA! \U00002716')

elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE VENCE! \U0001F44A')
    elif jogador == 1:
        print('COMPUTADOR VENCE! \U0000270C')
    elif jogador == 2:
        print('EMPATE! \U0001F91D')
    else:
        print('JOGADA INVÁLIDA! \U00002716')