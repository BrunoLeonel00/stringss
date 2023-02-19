# jogo de adivnhaçoes
import random


print('-=-' * 20)
print('vou pensar em um numero de um a dez, e vc tem q tentar advinhar')
print('-=-' * 20)
numero = random.randint(0, 10)
jogador = int(input('Digite um numero:'))
if numero == jogador:
    print('parabenns, voce acertou!')

else:
    print('GANHEI, o numero que estava pensando era {} nao {}'.format(numero, jogador))
    numero = random.randint(0, 10)
    segunda = int(input('Segunda chance:'))
    if numero == jogador:
        print('parabens, voce acertou')
    else:
        print('você nao tem sorte mesmo, o numero era {} nao {}'.format(numero, segunda))


