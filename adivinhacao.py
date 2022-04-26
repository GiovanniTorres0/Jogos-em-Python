import random


def jogar():
    imprime_mensagem_abertura()

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    elif (nivel == 3):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    tentativa(total_de_tentativas, numero_secreto, pontos)

    imprime_mensagem_finalizacao()


def imprime_mensagem_abertura():
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************")


def mensagem_derrota():
    print("\n*******VOCÊ PERDEU!!!******")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensagem_vitoria(pontos):
    print("PARABÉNS VOCÊ GANHOU E FEZ {} PONTOS".format(pontos))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def tentativa(total_de_tentativas, numero_secreto, pontos):
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("\nVocê deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            mensagem_vitoria(pontos)
            break
        else:
            if (maior):
                print("VocÊ errou! O seu chute foi maior do que o número secreto.")

            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        if(rodada == total_de_tentativas):
            mensagem_derrota()


def imprime_mensagem_finalizacao():
    print("\n***********")
    print('Fim de Jogo')
    print("***********")


if (__name__ == "__main__"):
    jogar()
