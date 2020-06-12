from random import randint

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
palpite_jogador = int(input("Diga um valor: "))
par_ou_impar_jogador = ""
par_ou_impar_jogador = input("P/I: ")


if par_ou_impar_jogador == "p" or "P":
    par_ou_impar_jogador = "PAR"
elif par_ou_impar_jogador == "i" or "I":
    par_ou_impar_jogador = "ÍMPAR"


palpite_computador = randint(0, 9)
soma = palpite_jogador + palpite_computador

if soma % 2 == 0:
    paridade_soma = "PAR"
elif soma % 2 == 1:
    paridade_soma = "ÍMPAR"

print("------------------------------")

print("Você jogou {} e o computador {}. Total de {} deu {}".format(palpite_jogador, palpite_computador, soma, paridade_soma))

print("------------------------------")

if paridade_soma == par_ou_impar_jogador:
    print("Você ganhou!")
elif paridade_soma != par_ou_impar_jogador:
    print("Você perdeu!")