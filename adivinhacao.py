import random

print("###################################")
print("Bem vindo ao jogo de Adivinhação")
print("###################################")

numero_secreto = random.randrange(1,101)
chance = 0
pontos = 1000

print("Qual o nivel de dificuldade ?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Escolha o nivel"))

if(nivel == 1):
    chance = 20
elif(nivel == 2):
    chance = 10
else:
    chance = 5

for rodada in range(1, chance + 1):
    print("Tentativa {} de {}" .format(rodada, chance))

    chute_str = input("Digite o número entre 1 e 100:")
    print("Você digitou " , chute_str)
    chute = int(chute_str)
    if(chute < 1 or chute > 100):
        print("você deve digirar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou e fez {} pontos!" .format(pontos))
        break
    else:
        if(maior):
            print("Você errou o seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou o seu chute foi menor que o numero secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do Jogo")
print(numero_secreto)

