import random

print('--------------------------------------------------')
print('-------- BEM VINDO AO JOGO DE ADIVINHAÇÃO --------')
print('--------------------------------------------------')

print('Regras: ')
print('Você começa a partida com 1000 pontos. A cada palpite incorreto, você perde')
print('a quantidade de pontos equivalente ao seu palpite.')
print('Tente terminar o jogo com o maior número de pontos')
print('--------------------------------------------------')
print('Niveis:')
print('Ao escolher o nível fácil você terá direito a 20 tentativas')
print('Ao escolher o nível médio você terá direito a 10 tentativas')
print('Ao escolher o nível dificíl você terá direito a 5 tentativas')
print('--------------------------------------------------')
print('--------------------------------------------------')
print('Escolha o nível de sua partida!')
print('Fácil [1] - Médio [2] - Dificíl [3]')
nivel = int(input(' '))

if (nivel == 1):
    numero_de_tentativas = 20
elif (nivel == 2):
    numero_de_tentativas = 10
else:
    numero_de_tentativas = 5

contador = 1
pontos = 1000
numero_secreto = random.randrange(1, 101)

print('-----INFORME UM VALOR ENTRE 1 E 100 ------')
for rodada in range(1, numero_de_tentativas + 1):
    palpite = int(input("Tentativa {}. Qual o seu palpite? ".format(contador)))
    if(palpite < 1 or palpite > 100):
      print("Você deve informar um numero válido. -----INFORME UM VALOR ENTRE 1 E 100 ------")
    else:
        if (palpite == numero_secreto):
           print('Parabens, você acertou o numero secreto!!!!!!!')
           print('Sua pontuação foi de {}'.format(pontos))
           break
        elif (palpite > numero_secreto):
           print('Seu palpite foi maior que o numero secreto!!')
           pontos = abs(pontos - palpite)
        else:
           print('Seu palpite foi menor que o numero secreto')
           pontos = abs(pontos - palpite)
    if (numero_de_tentativas == contador):
        print('Suas tentativas acabaram. Game Over')
    contador = contador + 1


