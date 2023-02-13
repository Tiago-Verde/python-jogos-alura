import forca
import adivinhacao

def escolhe_jogo():
    print('--------------------------------------------------')
    print('--------- SELECIONE SEU JOGO PREFERIDO!! ---------')
    print('--------------------------------------------------')

    jogo = int(input('[1] Forca - [2] Adivinhação '))
    print('                                        ')

    if(jogo == 1):
        forca.jogar()
    else:
        adivinhacao.jogar()


if(__name__ == "__main__"):
    escolhe_jogo()