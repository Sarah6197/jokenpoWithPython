from random import randint
from time import sleep

while True:
    jogadaPlayer =int(input('Escolha entre:\n=-=-=-=-=-=\n[0]PEDRA\n[1]PAPEL\n[2]TESOURA\n[3]SAIR\n=-=-=-=-=-=\n'))
    jogadaComputador = randint(0,2)
    jogadas = ['PEDRA', 'PAPEL', 'TESOURA']

    if jogadaPlayer == 3:
        break

    print('°' * 10)
    print('JO')
    sleep(0.5)
    print('   KEN')
    sleep(0.5)
    print('       PO!\n')
    sleep(0.5)
    print('°' * 10)
    sleep(0.3)
    
    if jogadaPlayer == jogadaComputador:
        print(f'O Computador jogou {jogadas[jogadaPlayer]}\n EMPATE!\n')
    elif jogadaPlayer == 0 and jogadaComputador != 1:
        print(f'O Computador jogou {jogadas[jogadaPlayer]}\n VOCÊ VENCEU!\n')
    elif jogadaPlayer == 1 and jogadaComputador != 2:
        print(f'O Computador jogou {jogadas[jogadaPlayer]} \n VOCÊ VENCEU!\n')
    elif jogadaPlayer == 2 and jogadaComputador != 0:
        print(f'O Computador jogou {jogadas[jogadaComputador]} \n VOCÊ VENCEU!\n')
    else:
        print(f'O Computador jogou {jogadas[jogadaComputador]} \n VOCÊ PERDEU!\n')






















