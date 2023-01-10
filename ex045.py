"""Crie um programa que faça o computador
jogar jokenpô com você.
pedra papel e tesoura"""
from random import randint
from time import sleep
print('='*10, 'JOKENPÔ', '='*10)
print('='*8, 'VAMOS JOGAR', '='*8)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('kEN')
sleep(1)
print('PÔ')
sleep(1)
print('='*30)
print('Você jogou {}.'.format(itens[jogador]))
print('O computador escolheu {}.'.format(itens[computador]))
print('='*30)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU1')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
