#importação

import time

#respostas
r1 = 23
r2 = 12
r3 = 40
#mensagem de boas vindas
print("bem vindo ao quiz de matemática!")
print()
time.sleep(1)
print("pronto?")
print()
time.sleep(1)
print("vamos começar!")
print()
time.sleep(1)

#pergunta 1

pergunta1 = input("quanto é 10 + 13? ")
print()
while pergunta1 != str(r1):
    time.sleep(0.5)
    print("validando...")
    print()
    time.sleep(2.5)
    print("resposta incorreta, tente novamente!")
    print()
    time.sleep(1)
    pergunta1 = input("quanto é 10 + 13? ")
    print()
    time.sleep(0.5)
print("validando...")
print()
time.sleep(2.5)
print("muito bem! a resposta está correta!")
print()
time.sleep(1)
print("vamos para a próxima pergunta!")
print()
time.sleep(2)

#pergunta 2

pergunta2 = input("quanto é 6 + 6? ")
print()
while pergunta2 != str(r2):
    time.sleep(0.5)
    print("validando...")
    print()
    time.sleep(2.5)
    print("resposta incorreta, tente novamente!")
    print()
    time.sleep(1)
    pergunta2 = input("quanto é 6 + 6? ")
    print()
    time.sleep(0.5)
print("validando...")
print()
time.sleep(2.5)
print("muito bem! a resposta está correta!")
print()

#pergunta 3

pergunta3 = input("quanto é 20 + 20? ")
print()
while pergunta3 != str(r3):
    time.sleep(0.5)
    print("validando...")
    print()
    time.sleep(2.5)
    print("resposta incorreta, tente novamente!")
    print()
    time.sleep(1)
    pergunta3 = input("quanto é 20 + 20? ")
    print()
    time.sleep(0.5)
print("validando...")
print()
time.sleep(2.5)
print("meus parabéns! você acertou todas as perguntas! aqui está o seu prêmio:")
print()
time.sleep(3.5)
print("🏆")