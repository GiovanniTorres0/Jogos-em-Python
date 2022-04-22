import forca
import adivinhacao


def escolhe_jogo():
    print("********************************")
    print("*******Escolha seu Jogo!********")
    print("********************************")

    print("(1) Adivinhação (2) Forca")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("\n Jogar Adivinhação")
        adivinhacao.jogar()
    elif (jogo == 2):
        print("\n Jogar Forca")
        forca.jogar()
if(__name__ == "__main__"):
    escolhe_jogo()